from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

PG_USER = 'flaskexampleuser'
PG_PW = 'flaskexamplepw'
PG_DB = 'flaskexample'
CONN = 'postgresql://{0}:{1}@localhost/{2}'.format(PG_USER, PG_PW, PG_DB)


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'super-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = CONN
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app