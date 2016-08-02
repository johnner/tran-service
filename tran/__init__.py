#!/usr/bin/env python
# coding: utf-8
"""
    Перед первым запуском требуется создать БД "tran"
    и локального пользователя.
    После чего создать таблицы, выполнив SQL-скрипты из папки /sql
"""
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
import tran.config as config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
app.config['CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config.update(JSON_AS_ASCII=False)
app.config.update(WTF_CSRF_CHECK_DEFAULT=False)

# CProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# подгружаем urls
import models, controllers
