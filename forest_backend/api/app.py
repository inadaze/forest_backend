""" Main module for running the Flask app"""

# import atexit
import logging
from flasgger import Swagger
from flask import Flask, Blueprint
from flask_restful import Api
from forest_backend.api.resources.seed_api import SeedApi, SeedsApi
from forest_backend.api.resources.branch_api import BranchApi
from forest_backend.api.resources.tree_api import TreeApi, TreesApi, TreeUpdateApi
from forest_backend.database.sql_db import db
#from forest_backend.scheduler.forest_scheduler import ForestScheduler


API_BP = Blueprint('api', __name__)
api = Api(API_BP)

api.add_resource(SeedApi, '/seed')
api.add_resource(BranchApi, '/branch')
api.add_resource(TreeApi, '/tree/<string:seed_word>')
api.add_resource(TreesApi, '/trees')
api.add_resource(TreeUpdateApi, '/tree')
api.add_resource(SeedsApi, '/seeds/<string:level>')

app = Flask(__name__)
app.config.from_pyfile('config.py')
Swagger(app)

app.register_blueprint(API_BP, url_prefix='/api')

#scheduler = ForestScheduler()
#scheduler.start_scheduler()
#atexit.register(lambda: scheduler.scheduler.shutdown())

db.init_app(app)

# TODO: setup this config in an external file to be reused by all loggers
app.logger.setLevel(logging.DEBUG)
FILE_HANDLER = logging.FileHandler('api.log')
FILE_HANDLER.setLevel(logging.DEBUG)
STREAM_HANDLER = logging.StreamHandler()
STREAM_HANDLER.setLevel(logging.ERROR)
FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
FILE_HANDLER.setFormatter(FORMATTER)
STREAM_HANDLER.setFormatter(FORMATTER)
app.logger.addHandler(FILE_HANDLER)
app.logger.addHandler(STREAM_HANDLER)
