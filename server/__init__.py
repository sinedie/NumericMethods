from flask import Flask
from .config import config

from .rutas import client, raices, ecuaciones, interpolacion, integracion


def create_app(*args):
    app = Flask(__name__, static_folder="spa", static_url_path="/spa")
    app.config.from_object(config)

    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(client)
    app.register_blueprint(raices)
    app.register_blueprint(ecuaciones)
    app.register_blueprint(interpolacion)
    app.register_blueprint(integracion)
