import os
from pathlib import Path

URL_EPARH = 'https://eparh.com/File/sklad.zip'
URL_GLOBAL = 'http://beta.globengineer.ru/files/%D0%9E%D1%81%D1%82%D0%B0%D1%82%D0%BA%D0%B8%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%BE%D0%B2%20%D0%BD%D0%B0%20%D1%81%D0%BA%D0%BB%D0%B0%D0%B4%D0%B5.xls'
BASE_DIR = Path(__file__).parent
BASE_URL = os.getenv('BASE_URL', default='http://127.0.0.1:5000/')


class Config(object):
    FLASK_APP = os.getenv('FLASK_APP', default='klemsan_app')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI', default='sqlite:///db.sqlite3'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='YOUR_SECRET_KEY')
