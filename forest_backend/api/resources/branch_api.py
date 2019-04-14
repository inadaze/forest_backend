from flask_restful import Resource
from flask import request
from database.models.branch_model import Branch, BranchSchema
from database.models.tree_model import Tree, TreeSchema
from database.sql_db import db

branches_schema = BranchSchema(many=True)
branch_schema = BranchSchema()

class BranchApi(Resource):
    def get(self, seed_id):
        branches = db.session.query(Branch).join(Tree, Branch.id==Tree.branch_id)
        branches = branches_schema.dump(branches).data
        return {'status': 'success', 'data': branches}, 200

    def put(self, seed_id):
        branch = request.get_json()
        branch = Branch(
            idea=branch['idea'],
            level=branch['level']
        )
        db.session.add(branch)
        db.session.flush()
        db.session.refresh(branch)
        tree = Tree(
            seed_id=seed_id,
            branch_id=branch.id
        )
        db.session.add(tree)
        db.session.commit()
        return { "status": 'success' }, 204