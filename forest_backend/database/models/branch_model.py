from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Sequence
from forest_backend.database.sql_db import db, ma


class Branch(db.Model):
    __tablename__ = 'branches'
    id = db.Column(db.Integer, primary_key=True)
    idea = db.Column(db.String(250), nullable=False)
    level = db.Column(db.Integer, primary_key=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    last_modified_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, idea, level):
        self.idea = idea
        self.level = level

class BranchSchema(ma.Schema):
    id = fields.Integer(required=True, dump_only=True)
    idea = fields.String(required=True, dump_only=True)
    level = fields.Integer(required=True, dump_only=True)
    creation_date = fields.DateTime()
    last_modified_date = fields.DateTime()
