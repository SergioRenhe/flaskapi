import datetime

import jwt
from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash

from models.users import Users, token_required

users_blueprint = Blueprint("users_blueprint", __name__)


@users_blueprint.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    hashed_password = generate_password_hash(data["password"])

    new_user = Users(name=data["name"], password=hashed_password)
    new_user.save()

    return jsonify({"message": "registered successfully"})


@users_blueprint.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"WWW.Authentication": 'Basic realm: "login required"'})

    user = Users.query.filter_by(name=auth.username).first()

    if check_password_hash(user.password, auth.password):
        token = jwt.encode(
            {
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(minutes=30),
                "name": user.name,
            },
            "secret_key",
            algorithm="HS256",
        )
        return jsonify({"token": token})

    return jsonify({"WWW.Authentication": 'Basic realm: "login required"'})


@users_blueprint.route("/token-test", methods=["GET"])
@token_required
def test():
    return jsonify({"test": "ok"})
