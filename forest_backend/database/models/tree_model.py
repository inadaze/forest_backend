from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Sequence
from forest_backend.database.sql_db import db, ma
from forest_backend.database.models.seed_model import SeedSchema
from forest_backend.database.models.tree_level_model import TreeLevelSchema


class Tree(db.Model):
    __tablename__ = 'trees'

    id = db.Column(db.Integer, primary_key=True)
    seed_id = db.Column(db.Integer, db.ForeignKey('seeds.id'))
    level_id = db.Column(db.Integer, db.ForeignKey('tree_levels.id'), default=0)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    last_modified_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    seed = db.relationship('Seed', back_populates='tree', uselist=False, lazy=True)
    tree_level = db.relationship('TreeLevel', back_populates='tree', uselist=False, lazy=True)

    def __init__(self, seed_id):
        self.seed_id = seed_id

class TreeSchema(ma.Schema):
    id = fields.Integer(required=True, dump_only=True)
    seed_id = fields.Integer(required=True, dump_only=True)
    seed = fields.Nested(SeedSchema())
    level_id = fields.Integer(required=True, dump_only=True)
    level = fields.Nested(TreeLevelSchema())
    creation_date = fields.DateTime()
    last_modified_date = fields.DateTime()