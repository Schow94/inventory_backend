from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_modus import Modus
from werkzeug import url_decode
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app)


if os.environ.get('ENV') == 'production':
    app.config.from_object('config.ProductionConfig')

else:
    app.config.from_object('config.DevelopmentConfig')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from project.items.views import items_blueprint_bp

Migrate(app, db)

app.register_blueprint(items_blueprint_bp, url_prefix='/items')


@app.route('/')
def root():
    return "You've reached the root route. Please visit '/items' route"
    
