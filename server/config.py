import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

FLASK_ENV = os.environ.get("FLASK_ENV", "development")
SECRET_KEY = os.environ.get("SECRET_KEY", "secret")


class Config:
    FLASK_ENV = FLASK_ENV
    SECRET_KEY = SECRET_KEY

    DEBUG = False
    TESTING = False


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    pass


if FLASK_ENV == "production":
    config = ProdConfig()
elif FLASK_ENV == "testing":
    config = TestConfig()
else:
    config = DevConfig()
