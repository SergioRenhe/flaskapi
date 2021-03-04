from http import HTTPStatus

from flask import jsonify
from marshmallow import ValidationError


def retrieve_all(model, schema):
    try:
        schema_obj = schema(many=True)
        result_set = model.query.all()
        payload = schema_obj.dump(result_set)
        return jsonify(payload), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR


def retrieve_one(model, schema, id):
    try:
        schema_obj = schema()
        obj = model.retrieve(id)
        payload = schema_obj.dump(obj)
        return jsonify(payload), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR


def create(model, schema, request):
    schema_obj = schema()
    validated_data = {}
    if request:
        payload = request.get_json()
        try:
            validated_data = schema_obj.load(payload)
        except ValidationError as e:
            return (
                jsonify({"error": e.messages, "valid_data": e.valid_data}),
                HTTPStatus.BAD_REQUEST,
            )
    try:
        obj = model(**validated_data)
        obj.save()
        response = schema_obj.dump(obj)
        return jsonify(response), HTTPStatus.CREATED
    except Exception as e:
        return (jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST)


def delete(model, schema, id):
    schema_obj = schema()
    try:
        obj = model.retrieve(id)
        if not obj:
            raise Exception("Object does not exist")
        obj.delete()
        payload = schema_obj.dump(obj)
        return jsonify(payload), HTTPStatus.OK
    except Exception as e:
        return (jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)
