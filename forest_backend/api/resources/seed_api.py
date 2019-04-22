from flask_restful import Resource
from flask import request
from forest_backend.database.models.seed_model import Seed, SeedSchema
from forest_backend.database.sql_db import db

seeds_schema = SeedSchema(many=True)
seed_schema = SeedSchema()

class SeedApi(Resource):
    def get(self, seed_id):
        seed = Seed.query.filter_by(word=seed_id)
        seed = seeds_schema.dump(seed).data
        return {'status': 'success', 'data': seed}, 200

    def put(self, seed_id):
        if not request.json:
            seed = Seed(
                word=seed_id
            )
            db.session.add(seed)
            db.session.commit()
            return {"status": 'success'}, 204
        if 'word' in request.json:
            seed = request.get_json()
            seed = Seed(
                word=seed['word']
            )
            db.session.add(seed)
            db.session.commit()
            return {"status": 'success'}, 204
        
        return {"status": 'failure'}, 400

class SeedsApi(Resource):
    def get(self):
        if not request.json:
            seeds = Seed.query.all()
            seeds = seeds_schema.dump(seeds).data
            return {'status': 'success', 'data': seeds}, 200
        if 'tree_level' in request.json and type(request.json['tree_level']) == int:
            tree_level = request.json.get('tree_level')
            new_seeds = db.session.query(Seed).filter(
                ~Seed.id.in_(
                    db.session.query(Tree.seed_id).join(Seed).filter(Seed.id==Tree.seed_id)
                )
            ).all()
            new_seeds = seeds_schema.dump(new_seeds).data
            return {'status': 'success', 'data': new_seeds}, 200