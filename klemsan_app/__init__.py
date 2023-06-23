from celery import Celery
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379'
CELERY_TASK_LIST = [
    'klemsan_app.utils',
]


def make_celery():
    celery = Celery(
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND'],
        include=CELERY_TASK_LIST,
    )
    TaskBase = celery.Task

    class FlaskTask(TaskBase):
        abstract = True

        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = FlaskTask
    return celery


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import error_handlers, views, utils
