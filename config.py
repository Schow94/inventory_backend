import os


class Config():
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgres://localhost/heroku-flask-inventory'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://localhost/flask_inventory'


class TestingConfig(Config):
    TESTING = True
