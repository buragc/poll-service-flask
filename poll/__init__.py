import os
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from . import models


def create_app(config_name=None):
    # Set the configuration object
    if config_name is None:
        config_name = os.environ.get('POLLSVC_CONFIG', 'development')
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)

    # register the main blueprint
    from .pollsvc import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # TODO: register the api blueprint

    return app