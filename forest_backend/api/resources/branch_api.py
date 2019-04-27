from flask_restful import Resource
from flask import request
from forest_backend.database.models.branch_model import Branch, BranchSchema
from forest_backend.database.models.tree_model import Tree, TreeSchema
from forest_backend.database.sql_db import db

branches_schema = BranchSchema(many=True)
branch_schema = BranchSchema()

class BranchApi(Resource):
    def get(self, tree_id):
        branches = db.session.query(Branch).join(Tree, Branch.id==Tree.branch_id)
        branches = branches_schema.dump(branches).data
        return {'status': 'success', 'data': branches}, 200

    def put(self):
        branch = request.get_json()
        branch = Branch(
            idea=branch['idea'],
            tree_id=branch['tree_id']
        )
        db.session.add(branch)
        db.session.flush()
        db.session.refresh(branch)
        # tree = Tree(
        #     seed_id=tree_id,
        #     branch_id=branch.id
        # )
        # db.session.merge(tree)
        db.session.commit()
        return { "status": 'success' }, 204

# TODO: need to add many branches at one time