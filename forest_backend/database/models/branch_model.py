""" Module containing the Branch Models for the Forest database """
from marshmallow import fields
from ..sql_db import db, ma

class Branch(db.Model):
    """ SQLAlchemy Model for Branch Model table in Forest database """

    __tablename__ = 'branches'

    id = db.Column(db.Integer, primary_key=True)
    tree_id = db.Column(db.Integer, db.ForeignKey('trees.id'))
    idea = db.Column(db.String(250), nullable=False)
    branch_level = db.Column(db.Integer, primary_key=False, default=1)
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

    tree = db.relationship('Tree', back_populates='branch', uselist=False, lazy=True)

    def __init__(self, idea, tree_id, branch_level=0):
        self.idea = idea
        self.tree_id = tree_id
        self.branch_level = branch_level

class BranchSchema(ma.Schema):
    """ Marshmellow Schema for Branch Table """
    id = fields.Integer(required=True, dump_only=True)
    tree_id = fields.Integer(required=True, dump_only=True)
    idea = fields.String(required=True, dump_only=True)
    branch_level = fields.Integer(required=True, dump_only=True)
    creation_date = fields.DateTime()
    last_modified_date = fields.DateTime()
