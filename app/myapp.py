from flask import Flask
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy
from .myconfig import config_by_name
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
flask_bcrypt = Bcrypt()

def create_app(config_name:str):
    app_ = Flask(__name__)    
    app_.config.from_object(config_by_name[config_name])
    
    db.init_app(app_)
    migrate.init_app(app_, db)
    flask_bcrypt.init_app(app_)
    
    return app_;
