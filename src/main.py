from sys import path

from flask import Flask

path += ["src"]


def create_app(config="BaseConfig"):
    app = Flask(__name__)
    app.config.from_object(f"config.{config}")
    register_blueprints(app)
    create_db(app)
    return app


def create_db(app):
    from models import db

    db.init_app(app)
    with app.app_context():
        db.create_all()


def register_blueprints(app):
    from views.cars import cars_blueprint
    from views.persons import persons_blueprint
    from views.users import users_blueprint

    app.register_blueprint(cars_blueprint)
    app.register_blueprint(persons_blueprint)
    app.register_blueprint(users_blueprint)


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
