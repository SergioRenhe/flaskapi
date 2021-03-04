from functools import wraps

import jwt
from flask import jsonify, request

from models import base, db


class Users(base.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"message": "a valid token is missing"})

        try:
            data = jwt.decode(token, "secret_key", algorithms=["HS256"])
            name = data.get("name")
            current_user = Users.query.filter_by(name=name).first()
            if not current_user:
                raise Exception("User not found")
        except Exception as e:
            return jsonify({"error": str(e)})
        return f(*args, **kwargs)

    return decorator
