import os

from app.application import create_app, db, migrate
from app import blueprint


env = str('dev') #os.getenv('BOILERPLATE_ENV') or 
app = create_app(env)
app.register_blueprint(blueprint)

app.app_context().push()

db.create_all() #created

migrate.init_app(app, db)

if __name__ == "__main__": 
    app.run(debug=True)