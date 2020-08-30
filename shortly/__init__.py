import os

from flask import Flask
from flask_mongoengine import MongoEngine
from .db import db
from .short import urls
from .error import error

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config['MONGODB_SETTINGS'] = {
        'db' : 'shortly'
    }
    db.init_app(app)

    app.register_blueprint(error)
    app.register_blueprint(urls)

    return app
