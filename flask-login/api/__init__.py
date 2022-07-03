from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

PG_USER = 'flaskexampleuser'
PG_PW = 'flaskexamplepw'
PG_DB = 'flaskexample'
CONN = 'postgresql://{0}:{1}@localhost/{2}'.format(PG_USER, PG_PW, PG_DB)


def create_app():
    app = Flask(__name__)

    
    spp.config['SECRET_KEY'] = 'super-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = CONN

    db.init_app(app)
