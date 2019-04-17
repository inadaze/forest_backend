from flask_restful import Resource
from flask import request
from forest_backend.database.models.seed_model import Seed, SeedSchema
from forest_backend.database.models.tree_model import Tree
from forest_backend.database.sql_db import db

seeds_schema = SeedSchema(many=True)
seed_schema = SeedSchema()

class SeedApi(Resource):
    def get(self, seed_id):
        seed = Seed.query.filter_by(word=seed_id)
        seed = seeds_schema.dump(seed).data
        return {'status': 'success', 'data': seed}, 200

    def put(self, seed_id):
        seed = request.get_json()
        #tree = Tree()
        #db.session.add(tree)
        #db.session.flush()
        #db.session.refresh(tree) 
        seed = Seed(
            word=seed['word']
            #tree=tree
        )
        db.session.add(seed)
        db.session.commit()
        return {"status": 'success'}, 204

class SeedsApi(Resource):
    def get(self):
        seeds = None
        if request.data:
            data = request.get_json()
            asdf = ""
        else:
            seeds = Seed.query.all()
        
        seeds = seeds_schema.dump(seeds).data
        return {'status': 'success', 'data': seeds}, 200