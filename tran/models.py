# coding: utf-8
"""
    Модели данных.
    Есть пользователи, и у пользователей есть словарик избранных слов,
    которые он будет повторять.
"""
from tran import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """ Модель пользователя """
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwdhash = db.Column(db.String(54))
    prefered_lang = db.Column(db.String(45))
    prefered_from_lang = db.Column(db.String(45))
    prefered_to_lang = db.Column(db.String(45))
    created_date = db.Column(db.DateTime, default=db.func.now())

    def __init__(self, email, password, firstname=None, lastname=None):
        self.email = email.lower()
        self.set_password(password)
        self.firstname = firstname
        self.lastname = lastname

    def set_password(self, password):
        """ солим и хэшируем пароль перед сохранением """
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    def __repr__(self):
        return '<User %r>' % (self.email)


class UserWord(db.Model):
    """ Модель слова """
    __tablename__ = 'user_words'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'))
    word = db.Column(db.String(255), nullable=False,)
    translation = db.Column(db.String(500), nullable=False,)
    language = db.Column(db.String(50), nullable=False)
    sound = db.Column(db.String(200))
    repeats = db.Column(db.Integer())
    last_repeat = db.Column(db.DateTime,
                            default=db.func.now(),
                            onupdate=db.func.now()
                            )
    trained = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=db.func.now())

    # mobile app sync fields
    mob_marked = db.Column(db.Integer, default=0)
    mob_flags = db.Column(db.String(100), default='')
    mob_retention_max = db.Column(db.Integer, default=0)
    mob_retention = db.Column(db.Integer, default=0)
    mob_incorrect = db.Column(db.Integer, default=0)
    mob_keyword = db.Column(db.String(100), default=0)
    list = db.Column(db.String(80), default='')
    example = db.Column(db.String(500), default='')
    updated_date = db.Column(db.DateTime, default=db.func.now())
    transcription = db.Column(db.String(100), default='')

    user = db.relationship('User',
        primaryjoin='UserWord.user_id == User.uid',
        backref=db.backref('words', lazy='dynamic'))

    def __repr__(self):
        return self.word
