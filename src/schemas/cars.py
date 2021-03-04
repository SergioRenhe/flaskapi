from marshmallow_enum import EnumField
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.cars import Car, CarColor, CarModel


class CarSchema(SQLAlchemyAutoSchema):
    color = EnumField(CarColor)
    model = EnumField(CarModel)

    class Meta:
        model = Car
        include_fk = True
