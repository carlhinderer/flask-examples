from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from http import HTTPStatus

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

    login_manager = LoginManager()
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        return jsonify({'message': 'Must authenticate.'}), HTTPStatus.UNAUTHORIZED

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
