""" Module containing the Tree Models for the Forest database """
from marshmallow import fields
from ..sql_db import db, ma
from .seed_model import SeedSchema
from .tree_level_model import TreeLevelSchema
from .branch_model import BranchSchema

class Tree(db.Model):
    """ SQLAlchemy Model for Tree Model table in Forest database """

    __tablename__ = 'trees'

    id = db.Column(db.Integer, primary_key=True)
    seed_id = db.Column(db.Integer, db.ForeignKey('seeds.id'))
    level_id = db.Column(db.Integer, db.ForeignKey('tree_levels.id'), default=0)
    creation_date = db.Column(
        db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        nullable=False
        )
    last_modified_date = db.Column(
        db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        nullable=False
        )

    seed = db.relationship('Seed', back_populates='tree', uselist=False, lazy=True)
    tree_level = db.relationship('TreeLevel', back_populates='tree', uselist=False, lazy=True)
    branch = db.relationship('Branch', back_populates='tree', uselist=True, lazy=True)

    def __init__(self, seed_id):
        self.seed_id = seed_id

class TreeSchema(ma.Schema):
    """ Marshmellow Schema for Branch Table """
    id = fields.Integer(required=True, dump_only=True)
    seed_id = fields.Integer(required=True, dump_only=True)
    seed = fields.Nested(SeedSchema())
    level_id = fields.Integer(required=True, dump_only=True)
    level = fields.Nested(TreeLevelSchema())
    branch = fields.Nested(BranchSchema(), many=True)
    creation_date = fields.DateTime()
    last_modified_date = fields.DateTime()
