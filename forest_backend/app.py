from flask import Flask, Blueprint
from flask_restful import Resource, Api
from resources.AddSeed import AddSeed

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(AddSeed, '/<string:seed_id>')
