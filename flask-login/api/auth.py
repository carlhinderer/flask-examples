from flask import Blueprint, jsonify, request
from flask_login import login_user
from http import HTTPStatus
from passlib.hash import pbkdf2_sha256

from .models import User
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    request_data = request.json
    email = request_data['email']
    password = request_data['password']

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'message': 'Email not found in our system.'}), HTTPStatus.NOT_FOUND
    if not pbkdf2_sha256.verify(password, user.password):
        return jsonify({'message': 'Incorrect password.'}), HTTPStatus.FORBIDDEN

    login_user(user)
    return jsonify({'message': 'Successfully logged in.'})


@auth.route('/signup', methods=['POST'])
def signup():
    request_data = request.json
    email = request_data['email']
    password = request_data['password']
    name = request_data['name']

    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'message': 'Email already exists in system.'}), HTTPStatus.FORBIDDEN

    new_user = User(email=email, password=pbkdf2_sha256.hash(password), name=name)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully.'}), HTTPStatus.CREATED


@auth.route('/logout')
def logout():
    return 'Logout'
