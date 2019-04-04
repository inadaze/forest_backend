from flask_restful import Resource
from flask import request

seeds = {}

class AddSeed(Resource):
    def get(self, seed_id):
        return {seed_id: seeds[seed_id]}

    def put(self, seed_id):
        seeds[seed_id] = request.get_json()
        return {seed_id: seeds[seed_id]}