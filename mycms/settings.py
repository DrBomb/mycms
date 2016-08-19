import os

class base_settings(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

class debug_settings(base_settings):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    
class react_settings(debug_settings):
    WEBPACK_SERVER = os.getenv("REACT")

