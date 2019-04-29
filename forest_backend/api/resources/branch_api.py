""" A Flask-restful Resource file for the Branch API """
from flask_restful import Resource
from flask import request
from forest_backend.database.models.branch_model import Branch, BranchSchema
from forest_backend.database.models.tree_model import Tree
from forest_backend.database.sql_db import db

BRANCHES_SCHEMA = BranchSchema(many=True)
BRANCH_SCHEMA = BranchSchema()

class BranchApi(Resource):
    """ Class for Branch api endpoint /branch """
    def get(self):
        """
        Definition for GET /branch
        ---
        parameters:
            - name: tree_id
              type: integer
              required: true
              description: id of the tree associated to the branch you want to fetch
            - name: idea
              type: string
              required: true
              description: the word associated to the branch you want to fetch
        responses:
            200:
                description: Branch fetched successfully
            400:
                description: no required parameters in payload
        """
        if not request.get_json():
            return {'status': 'failure'}, 400
        branch_req = request.get_json()
        if branch_req['tree_id']:
            # pylint: disable=E1101
            branch = db.session.query(Branch).join(Tree).filter(
                Tree.id == Branch.tree_id
                ).filter(
                    Branch.idea == branch_req['idea']
                ).first()
            branch = BRANCH_SCHEMA.dump(branch).data
            return {'status': 'success', 'data': branch}, 200


    def put(self):
        """
        Definition for PUT /branch
        ---
        parameters:
            - name: tree_id
              type: integer
              required: true
              description: id of the tree associated to the branch you want to create
            - name: idea
              type: string
              required: true
              description: the word associated to the branch you want to create
        responses:
            200:
                description: Branch createdd successfully
            400:
                description: no required parameters in payload
        """
        if not request.get_json() or not request.get_json()['idea'] or not request.get_json()['tree_id']:
            return {'status': 'failure'}, 400

        branch = request.get_json()
        branch = Branch(
            idea=branch['idea'],
            tree_id=branch['tree_id']
        )
        # pylint: disable=E1101
        db.session.add(branch)
        db.session.flush()
        db.session.refresh(branch)
        db.session.commit()
        return {"status": 'success'}, 204

# TODO: need to add and get many branches at one time
