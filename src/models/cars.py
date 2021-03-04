from enum import Enum, auto

from models import base, db, persons


class CarModel(Enum):
    HATCH = auto()
    SEDAN = auto()
    CONVERTIBLE = auto()


class CarColor(Enum):
    YELLOW = auto()
    BLUE = auto()
    GRAY = auto()


class Car(base.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.Enum(CarColor), nullable=False)
    model = db.Column(db.Enum(CarModel), nullable=False)
    owner_id = db.Column(
        db.Integer, db.ForeignKey(persons.Person.id), nullable=False
    )
    owner = db.relationship(persons.Person, backref="cars")

    def save(self):
        person = persons.Person.retrieve(self.owner_id)
        if person.sale_opportunity:
            super().save()
        else:
            raise Exception("Person has reached cars limit")
