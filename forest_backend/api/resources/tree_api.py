from flask_restful import Resource
from flask import request
from database.models.tree_model import Tree, TreeSchema
from database.models.branch_model import Branch, BranchSchema
from database.sql_db import db

trees_schema = TreeSchema(many=True)
tree_schema = TreeSchema()

class TreeApi(Resource):
    def get(self, seed_id):
        trees = Branch.query.all()
        trees = tree_schema.dump(trees).data
        return {'status': 'success', 'data': trees}, 200
