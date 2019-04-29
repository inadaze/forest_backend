from flask import Flask, Blueprint
from flask_restful import Resource, Api
import logging
from forest_backend.api.resources.seed_api import SeedApi, SeedsApi
from forest_backend.api.resources.branch_api import BranchApi
from forest_backend.api.resources.tree_api import TreeApi, TreesApi, TreeUpdateApi
from forest_backend.database.sql_db import db, ma
from forest_backend.scheduler.forest_scheduler import ForestScheduler
import atexit

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(SeedApi, '/seed')
api.add_resource(BranchApi, '/branch')
api.add_resource(TreeApi, '/tree/<string:seed_word>')
api.add_resource(TreesApi, '/trees')
api.add_resource(TreeUpdateApi, '/tree')
api.add_resource(SeedsApi, '/seeds/<string:level>')

app = Flask(__name__)
app.config.from_pyfile('config.py')

app.register_blueprint(api_bp, url_prefix='/api')

#scheduler = ForestScheduler()
#scheduler.start_scheduler()
#atexit.register(lambda: scheduler.scheduler.shutdown())

db.init_app(app)

# create logger with 'spam_application'
#logger = logging.getLogger('forest_backend_api')
app.logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('api.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
app.logger.addHandler(fh)
app.logger.addHandler(ch)
