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
    """ Class for Tree api endpoint /tree """
    def get(self, seed_word):
        """
        Definition for GET /tree
        Returns only branches of the tree that have not been cut
        ---
        paramaters:
            - name: seed_word
              type: string
              required: true
              description: word of the seed that grew the tree you want to fetch
        responses:
            200:
              description: Tree fetched successfully
            400:
              description: no required parameters in path
        """
        if not seed_word:
            return {'status': 'failure'}, 400
        app.logger.info('Fetching a Tree')
        tree = Tree.query.join(Seed).filter(
            Tree.seed_id == Seed.id
            ).filter(
                Seed.word == seed_word
            ).first()
        tree = TREE_SCHEMA.dump(tree).data
        for i, branch in enumerate(tree['branch']):
            if branch['cut'] == True:
                del tree['branch'][i]
        return {'status': 'success', 'data': tree}, 200

    def put(self, seed_word):
        """
        Definition for PUT /tree
        ---
        paramaters:
            - name: seed_word
              type: string
              required: true
              description: word of the seed that you want to create
        responses:
            200:
                description: Tree created successfully
            400:
                description: no required parameters in path
        """
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
    """ Class for Tree api endpoint /trees """
    def get(self):
        """
        Definition for GET /trees
        Fetch tree by level_id or all trees
        ---
        paramaters:
            - name: level_id
              type: int
              required: false
              description: fetch all trees with specified level
        responses:
            200:
              description: Trees fetched successfully
            400:
              description: no required parameters in payload
        """
        if not request.get_json():
            app.logger.info('Fetching all trees')
            trees = Tree.query.all()
            trees = TREES_SCHEMA.dump(trees).data
            return {'status': 'success', 'data': trees}, 200
        if 'level_id' in request.get_json():
            tree_level = request.get_json()['level_id']
            app.logger.info('Fetching all level %s trees', tree_level)
            # pylint: disable=E1101
            trees = db.session.query(Tree).join(Seed).filter(
                Tree.seed_id == Seed.id
                ).filter(
                    Tree.level_id == tree_level
                    ).all()
            trees = TREES_SCHEMA.dump(trees).data
            return {'status': 'success', 'data': trees}, 200
        return {'status': 'failure'}, 400

class TreeUpdateApi(Resource):
    """ Class for Tree api endpoint patch /tree """
    def patch(self):
        """
        Definition for PATCH /tree
        ---
        paramaters:
            - name: level_id
              type: int
              required: true
              description: level to upgrade tree to
            - name: id
              type: int
              required: true
              description: id of tree to upgrade level
        responses:
            200:
              description: Trees updated successfully
            404:
              description: no required parameters in payload
        """
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
