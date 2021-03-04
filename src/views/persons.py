from flask import Blueprint

from models.persons import Person
from schemas.persons import PersonSchema
from views.base import create, retrieve_all, retrieve_one

persons_blueprint = Blueprint("persons_blueprint", __name__)

model_schema = {"model": Person, "schema": PersonSchema}


@persons_blueprint.route("/persons", methods=["GET"])
def list_view():
    return retrieve_all(**model_schema)


@persons_blueprint.route("/persons/<int:id>", methods=["GET"])
def retrieve_view(id):
    return retrieve_one(**model_schema, id=id)


@persons_blueprint.route("/persons", methods=["POST"])
def create_view():
    return create(**model_schema, request=None)
