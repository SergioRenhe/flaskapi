import os


class BaseConfig:
    DEBUG = False
    db = {
        "user": os.getenv("POSTGRES_USER", "postgres"),
        "pw": os.getenv("POSTGRES_PASSWORD", "postgres"),
        "host": os.getenv("POSTGRES_HOST", "db"),
        "port": os.getenv("POSTGRES_PORT", 5432),
        "db": os.getenv("POSTGRES_DB", "postgres"),
    }
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % db
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite://"
