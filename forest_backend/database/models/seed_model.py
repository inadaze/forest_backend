""" Module containing the Seed Models for the Forest database """
from marshmallow import fields, validate
from ..sql_db import db, ma

class Seed(db.Model):
    """ SQLAlchemy Model for Seed Model table in Forest database """

    __tablename__ = 'seeds'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=True)
    word = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(
        db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        nullable=False
        )

    tree = db.relationship('Tree', back_populates='seed', uselist=False, lazy=True)

    def __init__(self, word, location):
        self.word = word
        self.location = location

class SeedSchema(ma.Schema):
    """ Marshmellow Schema for Seed Table """
    id = fields.Integer(required=True, dump_only=True)
    location = fields.String(required=False, dump_only=True)
    word = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()
