""" Module for executing flask-migrate scripts """
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from ..api.app import app
from .sql_db import db
from .inserts import populate

MIGRATION_DIR = os.path.join('forest_backend', 'database', 'migrations')

MIGRATE = Migrate(app, db, directory=MIGRATION_DIR)
# pylint: disable=C0103
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def populate_default_data():
    """ Function to populate the database with default data """
    populate(db)

if __name__ == '__main__':
    manager.run()
