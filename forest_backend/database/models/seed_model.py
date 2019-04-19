from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Sequence
from forest_backend.database.sql_db import db, ma


class Seed(db.Model):
    __tablename__ = 'seeds'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    tree = db.relationship('Tree', back_populates='seed', uselist=False, lazy=True)

    def __init__(self, word):
        self.word = word

class SeedSchema(ma.Schema):
    id = fields.String(required=True, dump_only=True)
    word = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()