from flask import Flask
from .config import config

from .routes.raices.routes import raices


def create_app(*args):

    app = Flask(__name__)
    app.config.from_object(config)

    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(raices)