# Web server for Tran:
- adds "favorite" functionality: api for all supported languages 
- user auth


## Installation:
sudo apt-get install mysql-server mysql-client

- git clone <proj_dir>
- virtualenv env
- . ./env/bin/activate
- pip install -r requirements.txt
- create `tran/config_local.py` for local settings (db connection, secret key, etc)


## DB:
 - GRANT ALL ON tran.* TO 'user'@'localhost';
 - `./manage.py db init` - создание приложения миграций
 - `./manage.py db migrate` - создать миграции (перед выполнением проверить их корректность)
 - `./manage.py db upgrade` - применить миграции к БД


## RUN:
- run server with `./run.py`

## Run tests:

`python test.py`