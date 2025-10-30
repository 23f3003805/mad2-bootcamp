from flask import Flask
from flask_cors import CORS
from models import db, User
from routes import api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "super-secret"
jwt = JWTManager(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_database.db'
db.init_app(app)

api.init_app(app)
# This is we do in mad1:
#  @app.route('/')
# def home():
#     return "Hello"

# This is we do in mad2: return data instead of html


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        admin=User.query.filter_by(email='admin@gamil.com').first()
        if not admin:
            admin=User(email='admin@gamil.com',password='adminpass', role='admin')
            db.session.add(admin)
            db.session.commit()
            print('Admin user created with email:admin@gamil.com and password:adminpass')
        else:
            print('Admin user already exists with email:admin@gamil.com and password:adminpass')
    app.run(debug = True)