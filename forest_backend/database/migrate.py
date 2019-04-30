from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from ..api.app import app
from .sql_db import db
from .inserts import populate
import os

MIGRATION_DIR = os.path.join('forest_backend', 'database', 'migrations')

migrate = Migrate(app, db, directory=MIGRATION_DIR)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def populate_default_data():
    populate(db)


if __name__ == '__main__':
    manager.run()