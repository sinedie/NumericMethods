from flask import Flask
from .config import config

from .blueprints.raices.routes import raices
from .blueprints.client.routes import client


def create_app(*args):

    app = Flask(__name__, static_folder="spa", static_url_path="/spa")
    app.config.from_object(config)

    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(raices)
    app.register_blueprint(client)