# coding: utf-8

from flask.ext.wtf import Form
from wtforms import (validators, PasswordField,
                     TextField, SubmitField, SelectField)

from tran.models import User

EMAIL_REQ_MSG = u'Пожалуйста, укажите адрес электронной почты'
PASS_REQ_MSG = u'Пожалуйста, задайте пароль'
REQ_FIELD_MSG = u'Обязательное поле'
EMAIL_EXIST_MSG = u'Такой email уже занят'
# EMAIL_REQ_MSG = 'Please enter your email'
# PASS_REQ_MSG = 'Please set your password'
# EMAIL_EXIST_MSG = 'That email is already taken'


class LoginForm(Form):
    email = TextField('Email',
                      [validators.Required(EMAIL_REQ_MSG),
                       validators.Email(EMAIL_REQ_MSG)
                       ]
                      )
    password = PasswordField('Password',
                             [validators.Required(REQ_FIELD_MSG)]
                             )
    submit = SubmitField(u'Войти')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user and user.check_password(self.password.data):
                return True
        else:
            self.email.errors.append(u'Неверное имя пользователя или пароль')
            return False


class SignupForm(Form):
    email = TextField('Email',
                      [validators.Required(EMAIL_REQ_MSG),
                       validators.Email(EMAIL_REQ_MSG)
                       ]
                      )
    password = PasswordField('Password',
                             [validators.Required(REQ_FIELD_MSG)]
                             )
    submit = SubmitField(u'Создать аккаунт')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append(EMAIL_EXIST_MSG)
            return False
        else:
            return True

LANG_CHOICES = [('english', u'Английский'),
                ('german', u'Немецкий'),
                ('french', u'Французский'),
                ('spain', u'Испанский'),
                ('italian', u'Итальянский'),
                ('turkish', u'Турецкий')
                ]


class ProfileForm(Form):
    word = TextField('Word',
                     [validators.Required(REQ_FIELD_MSG)]
                     )
    translation = TextField('Translation')
    language = SelectField(u'Язык', choices=LANG_CHOICES)
    sound = TextField('Sound')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        return True
