from flask_restful import Resource
from flask import request
from forest_backend.database.models.tree_model import Tree, TreeSchema
from forest_backend.database.models.seed_model import Seed
from forest_backend.database.models.branch_model import Branch, BranchSchema
from forest_backend.database.sql_db import db

trees_schema = TreeSchema(many=True)
tree_schema = TreeSchema()

class TreeApi(Resource):
    def get(self, seed_word):
        tree = db.session.query(Tree).join(Seed).filter(Tree.seed_id==Seed.id).filter(Seed.word==seed_word).first()
        tree = tree_schema.dump(tree).data
        return {'status': 'success', 'data': tree}, 200

    def put(self, seed_word):
        seed = db.session.query(Seed).filter(
            ~Seed.id.in_(
                db.session.query(Tree.seed_id).join(Seed).filter(Seed.id==Tree.seed_id)
            )
        ).filter(
                Seed.word==seed_word
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
            trees = Tree.query.all()
            trees = trees_schema.dump(trees).data
            return {'status': 'success', 'data': trees}, 200
        if 'level_id' in request.get_json():
            trees = db.session.query(Tree).join(Seed).filter(Tree.seed_id==Seed.id).filter(Tree.level_id==request.get_json()['level_id']).all()
            trees = trees_schema.dump(trees).data
            return {'status': 'success', 'data': trees}, 200