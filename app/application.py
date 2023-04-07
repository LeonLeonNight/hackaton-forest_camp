from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate
from .config import config_by_name
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
flask_bcrypt = Bcrypt()
migrate = Migrate()

def create_app(config_name:str):
    app = Flask(__name__)    
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    
    flask_bcrypt.init_app(app)
    
    manager = Manager(app)
    manager.add_command('db')
    
    return app;