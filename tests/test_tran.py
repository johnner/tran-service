#!/venv/bin/python
# coding: utf-8
import os
from tran import app
import unittest
import tempfile


class TranModelsTestCase(unittest.TestCase):
    def setUp(self):
        # генерим ссылку на дескриптор файла временной БД sqlite
        # и рандомное имя файла
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        app.init_db()

    def tearDown(self):
        # закрываем и удаляем файл с временной бд
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()


def run():
    unittest.main()
