from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Sequence
from forest_backend.database.sql_db import db, ma

#TODO: this needs to be migrated into the db
class TreeLevel(db.Model):
    __tablename__ = 'tree_levels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    tree = db.relationship('Tree', back_populates='tree_level', uselist=False, lazy=True)

    def __init__(self, level_id, name):
        self.id = level_id
        self.name = name

class TreeLevelSchema(ma.Schema):
    id = fields.String(required=True, dump_only=True)
    name = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()