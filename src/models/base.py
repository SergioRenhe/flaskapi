from models import db


class Model(db.Model):
    __abstract__ = True

    @classmethod
    def retrieve(cls, id):
        record = cls.query.get(id)
        return record

    @staticmethod
    def bulk_save(objects):
        db.session.bulk_save_objects(objects)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
