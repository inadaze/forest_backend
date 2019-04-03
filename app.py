from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

seeds = {}

class AddSeed(Resource):
    def get(self, seed_id):
        return {seed_id: seeds[seed_id]}

    def put(self, seed_id):
        seeds[seed_id] = request.get_json()
        return {seed_id: seeds[seed_id]}

api.add_resource(AddSeed, '/<string:seed_id>')

if __name__ == '__main__':
    app.run(debug=True)