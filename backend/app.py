from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_database.db'
db.init_app(app)

# This is we do in mad1:
#  @app.route('/')
# def home():
#     return "Hello"

# This is we do in mad2: return data instead of html
class HelloWorld(Resource):
    def get(self):
        return {'message': 'hello'}

api.add_resource(HelloWorld,'/message')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug = True)