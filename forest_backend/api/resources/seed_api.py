from flask_restful import Resource
from flask import request
from forest_backend.database.models.seed_model import Seed, SeedSchema
from forest_backend.database.models.tree_model import Tree
from forest_backend.database.sql_db import db

from flask import current_app as app

seeds_schema = SeedSchema(many=True)
seed_schema = SeedSchema()

class SeedApi(Resource):
    def get(self, seed_id):
        app.logger.info('Fetching a seed')
        seed = Seed.query.filter_by(word=seed_id).first()
        seed = seed_schema.dump(seed).data
        return {'status': 'success', 'data': seed}, 200

    def put(self, seed_id=''):
        app.logger.info('Adding a new seed')
        if not request.get_json():
            seed = Seed(
                word=seed_id
            )
            db.session.add(seed)
            db.session.commit()
            return {"status": 'success'}, 204
        if 'word' in request.get_json() and request.get_json()['word'] != '':
            seed = request.get_json()
            seed = Seed(
                word=seed['word']
            )
            db.session.add(seed)
            db.session.commit()
            return {"status": 'success'}, 204
        
        return {"status": 'failure'}, 400

class SeedsApi(Resource):
    def get(self, level=''):
        if level == 'all':
            app.logger.info('Fetching all seeds')
            seeds = Seed.query.all()
            seeds = seeds_schema.dump(seeds).data
            return {'status': 'success', 'data': seeds}, 200
        #TODO: can I do this without adding the json body?  like just an extra path param or something?
        if level == 'new':
            app.logger.info('Fetching all new seeds')

            #Get all seeds that don't have a tree
            new_seeds = db.session.query(Seed).filter(
                ~Seed.id.in_(
                    db.session.query(Tree.seed_id).join(Seed).filter(Seed.id==Tree.seed_id)
                )
            ).all()
            #new_seeds = db.session.query(Seed).join(Tree).filter(Seed.id==Tree.seed_id).filter(Tree.level_id==tree_level)
            new_seeds = seeds_schema.dump(new_seeds).data
            return {'status': 'success', 'data': new_seeds}, 200