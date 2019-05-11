from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import application
from app.models import db

migrate = Migrate(application, db)

manager = Manager(application)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(
    host='0.0.0.0', port=5000, use_debugger=True))

if __name__ == '__main__':
    manager.run()
