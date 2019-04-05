from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

class Seed(db.Model):
    __tablename__ = 'seeds'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, seed):
        self.seed = seed

class SeedSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    word = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()