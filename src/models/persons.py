from models import base, db


class Person(base.Model):
    id = db.Column(db.Integer, primary_key=True)

    @property
    def sale_opportunity(self):
        less_than_3 = len(self.cars) < 3
        return less_than_3
