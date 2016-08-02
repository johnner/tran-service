# coding: utf-8

SECRET_KEY = 'dev'
DATABASE_URI = 'mysql+pymysql://login:pass@localhost/tran'
CSRF_ENABLED = False

# импорт локальных настроек
try:
    from config_local import *
except ImportError:
    pass