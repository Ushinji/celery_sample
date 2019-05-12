import os
from flask import Flask


application = Flask(__name__)


env = os.getenv('RUN_MODE', 'development')
application.config['RUN_MODE'] = env

if (env == 'development'):
    application.config.from_object('app.config.development.Config')
elif (env == 'test'):
    application.config.from_object('app.config.test.Config')
else:
    raise Exception(f"env is required \'development\', \'test\'. env: {env}")


from celery import Celery  # nopep8


def make_celery(app):
    celery = Celery(app.import_name)
    celery.config_from_object('app.celeryconfig')
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


celery = make_celery(application)


@celery.task()
def add_together(a, b):
    return a + b


import app.views  # nopep8
