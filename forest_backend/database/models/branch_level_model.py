from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Sequence
from ..sql_db import db, ma

class BranchLevel(db.Model):
    __tablename__ = 'branch_levels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'))
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, level_id, name):
        self.id = level_id
        self.name = name

class BranchLevelSchema(ma.Schema):
    id = fields.String(required=True, dump_only=True)
    name = fields.String(required=True, validate=validate.Length(1))
    branch_id = fields.Integer(required=False)
    creation_date = fields.DateTime()