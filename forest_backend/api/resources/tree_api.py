from flask_restful import Resource
from flask import request
from forest_backend.database.models.tree_model import Tree, TreeSchema
from forest_backend.database.models.branch_model import Branch, BranchSchema
from forest_backend.database.sql_db import db

trees_schema = TreeSchema(many=True)
tree_schema = TreeSchema()

class TreeApi(Resource):
    def get(self, seed_id):
        trees = Branch.query.all()
        trees = tree_schema.dump(trees).data
        return {'status': 'success', 'data': trees}, 200

class TreesApi(Resource):
    def get(self):
        req = request.get_json()
        trees = Tree.query.filter_by(level_id=req['level'])
        trees = tree_schema.dump(trees).data
        return {'status': 'success', 'data': trees}, 200