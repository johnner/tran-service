#!/usr/bin/env python
# coding: utf-8
from flask import (render_template, redirect, request, Response, session, url_for, jsonify)
from tran import app, db
from tran.forms import LoginForm, SignupForm, ProfileForm, LANG_CHOICES
from tran.models import User, UserWord
from werkzeug.exceptions import abort
from routes.api import plugin
from utils import serialize_to_show, swap_translation

DEFAULT_USER_LANG = 'english'

@app.route('/')
@app.route('/index/')
def index():
    if 'email' not in session:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('profile'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(csrf_enabled=False)
    # если пользователь залогинен, ему не нужно показывать авторизацию
    if 'email' in session:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        # если форма не валидна, возвращает с ошибками
        if form.validate() is False:
            return render_template('login.html', form=form)
        else:
            session['email'] = form.email.data
            return redirect(url_for('profile'))
    elif request.method == 'GET':
        return render_template('login.html', form=form)


@app.route('/logout/', methods=['GET'])
def logout():
    if 'email' not in session:
        return redirect(url_for('login'))

    session.pop('email', None)
    return redirect(url_for('index'))


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    """ Создание нового аккаунта """
    form = SignupForm()
    # если пользователь залогинен, ему не нужно показывать авторизацию
    if 'email' in session:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        if form.validate() is False:
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
            session['email'] = newuser.email
            return redirect(url_for('profile'))
    elif request.method == 'GET':
        return render_template('signup.html', form=form)


@app.route('/profile/', methods=['GET', 'POST'])
def profile():
    """ Профиль, включает в себя словарь и повторялку """
    form = ProfileForm()

    if 'email' not in session:
        return redirect(url_for('login'))

    user = User.query.filter_by(email=session['email']).first()

    lang = DEFAULT_USER_LANG
    uLang = dict(LANG_CHOICES)[lang]

    if user is None:
        return redirect(url_for('signup'))
    else:
        return render_template('profile.html',
                               form=form,
                               # words=words,
                               lang=(lang, uLang)
                               )


@app.route('/api/v1/words/', methods=['GET', 'POST'])
def api_words():
    """
    API списка слов (получение, создание нового слова)
    !WARNING! используется мобильным приложением
    """
    user = User.query.filter_by(email=session['email']).first()
    if 'email' not in session:
        return abort(403, {'errors': 'Authorization required'})
    if request.method == 'GET':
            language = DEFAULT_USER_LANG
            words = query_words(user, language)
            swapped = swap_translation(words)
            result = [serialize_to_show(word) for z in (zip(words, swapped)) for word in z]
            response = jsonify(wordsList=result, total=len(words))
            return response

@app.route('/api/temp/words/', methods=['GET'])
def api_android_words():
    """ Временный отладочный метод для андроид приложения """
    user = User.query.filter_by(email='juliet.capulet2033@gmail.com').first()
    if request.method == 'GET':
            language = DEFAULT_USER_LANG
            words = query_words(user, language)
            swapped = swap_translation(words)
            result = [serialize_to_show(word) for z in (zip(words, swapped)) for word in z]
            response = jsonify(wordsList=result, total=len(words))
            return response

@app.route('/api/v2/words/', methods=['GET', 'POST'])
def api2_words():
    """
    API списка слов
    Отличие от v1 - при выводе слова не задваиваются обратной подстановкой word<=>translation
    """
    user = User.query.filter_by(email=session['email']).first()
    if not 'email' in session:
        return abort(403, {'errors': 'Authorization required'})
    if request.method == 'GET':
            language = DEFAULT_USER_LANG
            words = query_words(user, language)
            result = [serialize_to_show(word) for word in words]
            response = jsonify(wordsList=result, total=len(words))
            return response
    # Создание нового слова
    elif request.method == 'POST':
        try:
            word = _serialize_to_save(request.json)
            #FIXME передавать language с клиента
            word['language'] = DEFAULT_USER_LANG
            word_name = request.json.get('name', '').encode('utf-8')
            if not user_has_word(word_name, user):
                new_word = create_word(word, user)
                return Response(
                    response=jsonify(result={'name': new_word.word}),
                    status=201,
                    mimetype="application/json"
                )
            else:
                return abort(409, {
                    'errors': 'Word with given name already exist'
                })

        except Exception as e:
            print e
            return abort(400, {'errors': e})


def create_word(word, user):
    new_word = UserWord(**word)
    user.words.append(new_word)
    db.session.add_all([user, new_word])
    db.session.commit()
    return new_word





def _serialize_to_save(word):
    return {
        'word': word.get('name', '').encode('utf-8'),
        'translation': word.get('translation', '').encode('utf-8'),
        'sound': word.get('sound', '').encode('utf-8'),
        # createdDate: word.created_date, ТОЛЬКО

        # для mobile api
        # выводить не нужно, но хранить в бд
        'last_repeat': word.get('testedDate', 0),
        'mob_marked': word.get('marked', 0),
        'mob_flags': word.get('flags', 0),
        'mob_retention_max': word.get('retentionMax', 0),
        'mob_retention': word.get('retention', 0),
        'mob_incorrect': word.get('incorrect', 0),
        'mob_keyword': word.get('keyword', ''),
        'example': word.get('example', ''),

        'list': word.get('list', ''),
        'transcription': word.get('transcription', '')
    }

# TODO: заменить на метод DELETE в /api/v1/words/
@app.route('/api/v1/removeword/', methods=['POST'])
def api_remove_word():
    """ API - Удаление слова из словаря пользователя """
    data = request.json
    word_id = data.get('id')
    entity = UserWord.query.filter(UserWord.id == word_id).first()

    if entity:
        db.session.delete(entity)
        db.session.commit()
        response = jsonify(result={'id': word_id})
    else:
        response = abort(404, {'errors': 'No item with requested id'})
    return response


@app.route('/export/', methods=['GET'])
def export():
    user = User.query.filter_by(email=session['email']).first()
    language = DEFAULT_USER_LANG
    word_ids = request.args.getlist('w')
    if word_ids:
        words = query_words(user, language, word_ids)
    else:
        words = query_words(user, language, None)
    result = []
    for word in words:
        result.append({
            'marked': 0,
            'keyWord': '',
            'transcription': '',
            'id': word.id,
            'date': 0,
            'translation': word.translation,
            'name': word.word,
            'sound': word.sound
        })
    response = jsonify(wordsList=result)
    # возвращаем файл
    response.headers["Content-Disposition"] = "attachment; filename=data.data"
    response.headers['Content-Type'] = 'text/css; charset=utf-8'
    return response


# FIXME: ограничение GET в 100 слов
@app.route('/api/v1/export/', methods=['GET'])
def api_export():
    """ Экспорт слов в файл """
    user = User.query.filter_by(email=session['email']).first()
    language = DEFAULT_USER_LANG
    words = query_words(user, language)
    result = [{
              'marked': 0,
              'keyWord': '',
              'transcription': '',
              'id': word.id,
              'date': 0,
              'translation': word.translation,
              'name': word.word,
              'sound': word.sound} for word in words]
    response = jsonify(wordsList=result)

    # This is the key: Set the right header for the response
    # to be downloaded, instead of just printed on the browser
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response


def query_words(user, language, filter_list=None):
    """ Запрашивает слова пользователя из БД """
    if filter_list:
        words = user.words.order_by(
            UserWord.id.desc()).filter(UserWord.id.in_(filter_list))
    else:
        words = user.words.order_by(UserWord.id.desc()).all()
    return words


def user_has_word(word, user):
    exist = user.words.filter(UserWord.word == word.lower()).first()
    if exist:
        return True
    else:
        return False
