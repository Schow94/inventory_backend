from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_modus import Modus
from werkzeug import url_decode
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask_inventory'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from project.items.views import items_blueprint

Migrate(app, db)

app.register_blueprint(items_blueprint, url_prefix='/items')


# @app.route('/')
# def root():
#     return "You've reached the root route"
    
