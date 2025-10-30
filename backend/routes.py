from flask_restful import Api, Resource
from flask import request
from models import db, Pizza,User

api = Api()

# for mad2 we return data instead of html
class HelloWorld(Resource):
    def get(self):
        return {'message': 'hello'}

api.add_resource(HelloWorld,'/message')


#authentication endpoints
class Registration(Resource):
    def post(self):
        data =request.get_json()
        if not data or 'email' not in data or 'password' not in data:
            return {'message':'email and password both are required'},404
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return {'message': 'User already exists!'}, 400
    
        new_user=User(email=data.get('email'),password=data.get('password'), role='admin')
        db.session.add(new_user)
        db.session.commit()
        return {'message':'user registered successfully'}

api.add_resource(Registration,'/register')
        

class PizzaApi(Resource):
    def get(self, pizza_id=None):
        if pizza_id : 
            pizza = Pizza.query.get(pizza_id)
            if not pizza:
                return {'message': 'Pizza not found!'}, 404
            return {'id': pizza.id, 'name': pizza.name, 'toppings': pizza.toppings}, 200
            
        pizzas = Pizza.query.all()
        pizzas = [{'name': p.name, 'toppings' : p.toppings} for p in pizzas]
        return {'message' : 'Pizzas fetched successfully', 'data' : pizzas},200
    
    
    def post(self):
        data = request.get_json()
        if not data or 'name' not in data and not data['name']:
            return {'message': 'Name is required!'}, 400
        
        pizza = Pizza(name=data['name'], toppings=data.get('toppings', False))
        db.session.add(pizza); db.session.commit()
        return {'message': 'Pizza created!'}, 201
    
    
    def put(self, pizza_id=None):
        if pizza_id is None:
            return {'message': 'Pizza ID is required for update!'}, 400
    
        pizza = Pizza.query.get(pizza_id)
        if not pizza:
            return {'message': 'Pizza not found!'}, 404
        
        data = request.get_json()
        if not data:
            return {'message': 'Date is required!'}, 400
        
        pizza.name = data.get('name', pizza.name)
        pizza.toppings = data.get('toppings', pizza.toppings)
        db.session.commit()
        return {'message': 'Pizza updated!'}, 200
    
    
    def delete(self, pizza_id=None):
        if pizza_id is None:
            return {'message': 'Pizza ID is required for deletion!'}, 400
        
        pizza = Pizza.query.get(pizza_id)
        if not pizza:
            return {'message': 'Pizza not found!'}, 404

        db.session.delete(pizza); db.session.commit()
        return {'message': 'Pizza deleted!'}, 200
    
    
api.add_resource(PizzaApi, '/pizza', '/pizza/<int:pizza_id>')