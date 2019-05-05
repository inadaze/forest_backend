""" Script to reset database """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from forest_backend.database.inserts import resetDatabase

if __name__ == '__main__':
    ENGINE = create_engine("postgresql://jasons:password@localhost/forest")
    SESSION = sessionmaker(bind=ENGINE)
    SESSION = SESSION()
    resetDatabase(ENGINE)