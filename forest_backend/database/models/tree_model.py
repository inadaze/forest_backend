from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Sequence
from forest_backend.database.sql_db import db, ma
from forest_backend.database.models.seed_model import SeedSchema


class Tree(db.Model):
    __tablename__ = 'trees'
    id = db.Column(db.Integer, primary_key=True)
    seed_id = db.Column(db.Integer, db.ForeignKey('seeds.id'))
    #branches = db.relationship('Branch', backref='tree', lazy=True)
    #tree_level = db.relationship('Tree_Level', backref='tree', lazy=True, uselist=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    last_modified_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    seed = db.relationship('Seed', back_populates='tree', uselist=False, lazy=True)

    def __init__(self, seed_id):
        self.seed = seed_id
    #    self.branches = branch_id
    #    self.tree_level = level_id

class TreeSchema(ma.Schema):
    id = fields.Integer(required=True, dump_only=True)
    seed_id = fields.Integer(required=True, dump_only=True)
    seed = fields.Nested(SeedSchema())
    #tree_level = fields.Integer(required=True, dump_only=True)
    creation_date = fields.DateTime()
    last_modified_date = fields.DateTime()