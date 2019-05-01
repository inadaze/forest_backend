""" A Flask-restful Resource file for the Seed API """
from flask_restful import Resource
from flask import request
from flask import current_app as app
from ...database.models.seed_model import Seed, SeedSchema
from ...database.models.tree_model import Tree
from ...database.sql_db import db

SEEDS_SCHEMA = SeedSchema(many=True)
SEED_SCHEMA = SeedSchema()

class SeedApi(Resource):
    """ Class for Seed api endpoint /seed """
    def get(self):
        """
        Definition for GET /seed
        ---
        paramaters:
            - name: id
              type: integer
              required: true
              description: id of the seed you are fetching
            - name: word
              type: string
              required: true
              description: the word that is the source of the tree
        responses:
            200:
              description: Seed fetched successfully
            400:
              description: no required parameters in payload
        """
        app.logger.info('Fetching a seed')
        if not request.get_json():
            return {"status": 'failure'}, 400
        json_data = request.get_json()
        if 'id' in request.get_json() and json_data['id'] != '':
            seed = Seed.query.filter(Seed.id == json_data['id']).first()
            seed = SEED_SCHEMA.dump(seed).data
            return {'status': 'success', 'data': seed}, 200
        if 'word' in request.get_json() and json_data['word'] != '':
            seeds = Seed.query.filter(Seed.word == json_data['word']).all()
            seeds = SEEDS_SCHEMA.dump(seeds).data
            return {'status': 'success', 'data': seeds}, 200
        return {"status": 'failure'}, 400

    def put(self):
        """
        Definition for PUT /seed
        ---
        parameters:
            - name: idea
              type: string
              required: true
              description: the word associated to the branch you want to create
            - name: location
              type: string
              required: true
              description: string representation of the location vector of the seed
        responses:
            200:
                description: Seed created successfully
            400:
                description: no required parameters in payload
        """
        app.logger.info('Adding a new seed')
        if not request.get_json():
            return {"status": 'failure'}, 400
        if ('word' in request.get_json() and request.get_json()['word'] != '' and
                'location' in request.get_json() and request.get_json()['location'] != ''):
            seed = request.get_json()
            seed = Seed(
                word=seed['word'],
                location=seed['location']
            )
            # pylint: disable=E1101
            db.session.add(seed)
            db.session.commit()
            return {"status": 'success'}, 204

        return {"status": 'failure'}, 400

class SeedsApi(Resource):
    """ Class for Seeds api endpoint /seeds """
    def get(self, level=''):
        """
        Definition for GET /seeds
        ---
        paramaters:
            - name: level
              type: string
              required: true
              description: subset of seeds to fetch (all|new)
        responses:
            200:
              description: Seed fetched successfully
            400:
              description: no required parameters in payload
        """
        if level == 'all':
            app.logger.info('Fetching all seeds')
            seeds = Seed.query.all()
            seeds = SEEDS_SCHEMA.dump(seeds).data
            return {'status': 'success', 'data': seeds}, 200
        if level == 'new':
            app.logger.info('Fetching all new seeds that do not have a tree')

            # pylint: disable=E1101
            new_seeds = db.session.query(Seed).filter(
                ~Seed.id.in_(
                    db.session.query(Tree.seed_id).join(Seed).filter(Seed.id == Tree.seed_id)
                )
            ).all()
            new_seeds = SEEDS_SCHEMA.dump(new_seeds).data
            return {'status': 'success', 'data': new_seeds}, 200
        # TODO: Should I be catching this or does flask always do it?
        return {'status': 'failure'}, 400
