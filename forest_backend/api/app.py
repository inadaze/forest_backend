from flask import Flask, Blueprint
from flask_restful import Resource, Api
from forest_backend.api.resources.seed_api import SeedApi
from forest_backend.api.resources.branch_api import BranchApi
from forest_backend.api.resources.tree_api import TreeApi
from forest_backend.database.sql_db import db, ma
from forest_backend.scheduler.scheduler import ForestScheduler
import atexit

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(SeedApi, '/<string:seed_id>')
api.add_resource(BranchApi, '/branch/<string:seed_id>')
api.add_resource(TreeApi, '/tree/<string:seed_id>')

app = Flask(__name__)
app.config.from_pyfile('config.py')

app.register_blueprint(api_bp, url_prefix='/api')

scheduler = ForestScheduler()
atexit.register(lambda: scheduler.scheduler.shutdown())

db.init_app(app)
