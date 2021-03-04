from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from models.persons import Person


class PersonSchema(ModelSchema):
    sale_opportunity = fields.Method("get_sale_opportunity")

    class Meta:
        model = Person
        include_relationships = True

    def get_sale_opportunity(self, obj):
        return obj.sale_opportunity
