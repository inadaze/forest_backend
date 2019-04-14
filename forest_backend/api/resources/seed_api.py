from flask_restful import Resource
from flask import request
from database.models.seed_model import Seed, SeedSchema
from database.sql_db import db

seeds_schema = SeedSchema(many=True)
seed_schema = SeedSchema()

class SeedApi(Resource):
    def get(self, seed_id):
        seeds = Seed.query.all()
        seeds = seeds_schema.dump(seeds).data
        return {'status': 'success', 'data': seeds}, 200

    def put(self, seed_id):
        seed = request.get_json()
        seed = Seed(
            seed_id=seed_id,
            word=seed['word']
        )
        db.session.add(seed)
        db.session.commit()
        return { "status": 'success' }, 204