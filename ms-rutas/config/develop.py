class Config(object):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///rutas.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False