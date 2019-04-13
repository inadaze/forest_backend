from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Sequence
from forest_backend.database.sql_db import db, ma

class Tree(db.Model):
    __tablename__ = 'trees'
    id = db.Column(db.Integer, primary_key=True)
    seed_id = db.Column(db.String(250), nullable=False)
    branch_id = db.Column(db.Integer, primary_key=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    last_modified_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, seed_id, branch_id):
        self.seed_id = seed_id
        self.branch_id = branch_id

class TreeSchema(ma.Schema):
    seed_id = fields.String(required=True, dump_only=True)
    branch_id = fields.Integer(required=True, dump_only=True)
    creation_date = fields.DateTime()
    last_modified_date = fields.DateTime()