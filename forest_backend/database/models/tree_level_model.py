""" Module containing the Tree Level Models for the Forest database """
from marshmallow import fields, validate
from ..sql_db import db, ma

class TreeLevel(db.Model):
    """ SQLAlchemy Model for Tree Model table in Forest database """

    __tablename__ = 'tree_levels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(
        db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        nullable=False
        )

    tree = db.relationship('Tree', back_populates='tree_level', uselist=False, lazy=True)

    def __init__(self, level_id, name):
        # pylint: disable=C0103
        self.id = level_id
        self.name = name

class TreeLevelSchema(ma.Schema):
    """ Marshmellow Schema for Tree Level Table """
    id = fields.String(required=True, dump_only=True)
    name = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()
