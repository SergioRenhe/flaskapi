from flask import Blueprint, request

from models.cars import Car
from models.users import token_required
from schemas.cars import CarSchema
from views.base import create, delete, retrieve_all, retrieve_one

cars_blueprint = Blueprint("cars_blueprint", __name__)

model_schema = {"model": Car, "schema": CarSchema}


@cars_blueprint.route("/cars", methods=["GET"])
def list_view():
    return retrieve_all(**model_schema)


@cars_blueprint.route("/cars/<int:id>", methods=["GET"])
@token_required  # Only secured this route to show the authentication working
def retrieve_view(id):
    return retrieve_one(**model_schema, id=id)


@cars_blueprint.route("/cars", methods=["POST"])
def create_view():
    return create(**model_schema, request=request)


@cars_blueprint.route("/cars/<int:id>", methods=["DELETE"])
def delete_view(id):
    return delete(**model_schema, id=id)
