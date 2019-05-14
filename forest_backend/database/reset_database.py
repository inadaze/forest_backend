""" Script to reset database """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from forest_backend.database.inserts import resetDatabase
from forest_backend.database.migrate import db

if __name__ == '__main__':
    ENGINE = create_engine("postgresql://jasons:password@localhost/forest")
    SESSION = sessionmaker(bind=ENGINE)
    SESSION = SESSION()
    resetDatabase(ENGINE)
    print("Now you need to run migrate.py")
    # Need to run migrate.py after this?