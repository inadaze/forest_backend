from flask_restful import Resource
from flask import request
from forest_backend.database.models.branch_model import Branch, BranchSchema
from forest_backend.database.models.tree_model import Tree, TreeSchema
from forest_backend.database.sql_db import db

branches_schema = BranchSchema(many=True)
branch_schema = BranchSchema()

class BranchApi(Resource):
    def get(self):
        if not request.get_json():
            return {'status': 'failure'}, 400
        branch_req = request.get_json()
        if branch_req['tree_id']:
            branch = db.session.query(Branch).join(Tree).filter(Tree.id==Branch.tree_id).filter(Branch.idea==branch_req['idea']).first()
            branch = branch_schema.dump(branch).data
            return {'status': 'success', 'data': branch}, 200


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

# TODO: need to add and get many branches at one time
