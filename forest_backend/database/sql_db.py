""" Global module for db an ma objects (probably not necessary """
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# pylint: disable=C0103
ma = Marshmallow()
db = SQLAlchemy()
