import os
from flask import Flask


application = Flask(__name__)


env = os.getenv('RUN_MODE', 'development')
application.config['RUN_MODE'] = env

application.config.from_object('app.config.BaseConfig')

import app.views  # nopep8
