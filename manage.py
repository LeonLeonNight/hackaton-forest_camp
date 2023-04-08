from flask_script import Manager
from flask_migrate import Migrate
from app.myapp import create_app, db

env = str('dev')
app = create_app(env)

manager = Manager(app)
manager.add_command('db')

if __name__ == '__main__':
    manager.run()