from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Pizza(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name =db.Column(db.String(80), nullable=False)
    toppings = db.Column(db.Boolean, nullable=True)
    
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True, nullable=True)
    password= db.Column(db.String(120), nullable=False)
    role =db.Column(db.String(20))
    