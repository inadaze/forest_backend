from flask import Flask, Blueprint
from flask_restful import Resource, Api
from resources.AddSeed import AddSeed

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(AddSeed, '/<string:seed_id>')


app = Flask(__name__)
app.config.from_object("config")


from app import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from Model import db
db.init_app(app)


# if __name__ == "__main__":
#     app = create_app()
    #app.run(debug=True)
