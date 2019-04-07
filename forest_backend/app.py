from flask import Flask, Blueprint
from flask_restful import Resource, Api
from resources.AddSeed import AddSeed
from resources.AddBranch import AddBranch
from resources.TreeApi import TreeApi

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(AddSeed, '/<string:seed_id>')
api.add_resource(AddBranch, '/branch/<string:seed_id>')
api.add_resource(TreeApi, '/tree/<string:seed_id>')

app = Flask(__name__)
app.config.from_object("config")


from app import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from Model import db
db.init_app(app)

import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


scheduler = BackgroundScheduler()
scheduler.add_job(func=print_date_time, trigger="interval", seconds=3)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


# if __name__ == "__main__":
#     app = create_app()
    #app.run(debug=True)
