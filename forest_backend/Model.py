from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Sequence

ma = Marshmallow()
db = SQLAlchemy()

class Seed(db.Model):
    __tablename__ = 'seeds'
    id = db.Column(db.Integer, primary_key=True)
    seed_id = db.Column(db.String(250), nullable=False)
    word = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, seed_id, word):
        self.seed_id = seed_id
        self.word = word

class SeedSchema(ma.Schema):
    seed_id = fields.String(required=True, dump_only=True)
    word = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()

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
