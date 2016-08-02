# coding: utf-8
from tran import app
from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand
import click

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@click.command()
@click.option('--port', default=9000, help='Server port number')
def main(port):
    app.run(debug=True, host='0.0.0.0', port=port)

# Запуск приложения UWSGI
if __name__ == '__main__':
    main()
