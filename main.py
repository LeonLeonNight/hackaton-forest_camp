import os

from flask_migrate import Migrate

from app import blueprint
from app.myapp import create_app, db

env = str('dev') #os.getenv('BOILERPLATE_ENV') or 
app = create_app(env)
app.app_context().push()

#app.register_blueprint(blueprint)

#db.create_all() #created

if __name__ == "__main__": 
    app.run(debug=True)