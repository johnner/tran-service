# coding: utf-8

from flask import (request, jsonify)
from tran import app, db
from tran.models import User, UserWord
import jwt
from werkzeug.exceptions import HTTPException, abort


@app.route('/api/user/', methods=['GET', 'POST'])
def user():
    """ идентифицируем пользователя, получая JWT в теле запроса """
    if request.method == 'GET':
        headers = request.headers.get('X-AUTH-TOKEN')
        if headers:
            login = jwt.decode(headers, 'secret', algorithm='HS256')
            user = User.query.filter_by(email=login['login']).first()
            if user:
                return 'OK!'
            else:
                return abort(403, {'errors': 'Unauthorized'})
        else:
            return abort(403, {'errors': 'Unauthorized'})
    elif request.method == 'POST':
        data = request.get_json(force=True)
        if data['login'] and data['password']:
            user = User.query.filter_by(email=data['login']).first()
            if user and user.check_password(data['password']):
                encoded = jwt.encode({'login': data['login']}, 'secret', algorithm='HS256')
                return encoded
            else:
                return abort(403, {'errors': 'Bad username or password'})
        else:
            return abort(403, {'errors': 'Bad username or password'})


@app.route('/api/plugin/add_word/', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return abort(400, {'errors': 'Not allowed'})
    elif request.method == 'POST':
        print '================ YOTZ! ================'
        return 'ok'