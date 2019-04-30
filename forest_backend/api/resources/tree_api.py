""" A Flask-restful Resource file for the Tree API """
from flask_restful import Resource
from flask import request
from flask import current_app as app
from ...database.models.tree_model import Tree, TreeSchema
from ...database.models.seed_model import Seed
from ...database.sql_db import db

TREES_SCHEMA = TreeSchema(many=True)
TREE_SCHEMA = TreeSchema()

class TreeApi(Resource):
    def get(self, seed_word):
        app.logger.info('Fetching a Tree')
        tree = Tree.query.join(Seed).filter(Tree.seed_id == Seed.id).filter(Seed.word == seed_word).first()
        tree = TREE_SCHEMA.dump(tree).data
        return {'status': 'success', 'data': tree}, 200

    def put(self, seed_word):
        app.logger.info('Creating a new Tree')
        # pylint: disable=E1101
        seed = db.session.query(Seed).filter(
            ~Seed.id.in_(
                db.session.query(Tree.seed_id).join(Seed).filter(Seed.id == Tree.seed_id)
            )
        ).filter(
                Seed.word == seed_word
            ).first()
        if not seed:
            return {"status": 'not found'}, 404
        tree = Tree(seed.id)
        db.session.add(tree)
        db.session.commit()
        return {"status": 'success'}, 204

class TreesApi(Resource):
    def get(self):
        if not request.get_json():
            app.logger.info('Fetching all trees')
            trees = Tree.query.all()
            trees = TREES_SCHEMA.dump(trees).data
            return {'status': 'success', 'data': trees}, 200
        if 'level_id' in request.get_json():
            tree_level = request.get_json()['level_id']
            app.logger.info('Fetching all level %s trees', tree_level)
            # pylint: disable=E1101
            trees = db.session.query(Tree).join(Seed).filter(Tree.seed_id == Seed.id).filter(Tree.level_id == tree_level).all()
            trees = TREES_SCHEMA.dump(trees).data
            return {'status': 'success', 'data': trees}, 200

class TreeUpdateApi(Resource):
    def patch(self):
        app.logger.info('Updating tree')
        if not request.get_json():
            return {'status': 'failure'}, 404
        tree_req = request.get_json()
        # pylint: disable=E1101
        tree = db.session.query(Tree).filter(Tree.id == tree_req['id']).first()
        tree.level_id = tree_req['level_id']
        db.session.merge(tree)
        db.session.commit()
        return {'status': 'success'}, 200