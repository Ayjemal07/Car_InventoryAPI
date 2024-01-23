from flask import Blueprint, request, jsonify, render_template
from app.helpers import token_required
from app.models import db, User, Car, contact_schema, contacts_schema

api = Blueprint('api',__name__, url_prefix='/api')

# @api.route('/getdata')
# def getdata():
#     return {'yee': 'haw'}

@api.route('/cars', methods = ['POST'])
@token_required
def create_car(current_user_token):

    make = request.json['make']
    year = request.json['year']
    model = request.json['model']
    features = request.json['features']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    car = Car(make, year, model, features, user_token = user_token )

    db.session.add(car)
    db.session.commit()

    response = contact_schema.dump(car)
    return jsonify(response)


@api.route('/cars', methods = ['GET'])
@token_required
def get_cars(current_user_token):
    a_user = current_user_token.token
    cars= Car.query.filter_by(user_token = a_user).all()
    response = contacts_schema.dump(cars)
    return jsonify(response)

@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_single_car(current_user_token,id):
    car = Car.query.get(id)
    response = contact_schema.dump(car)
    return jsonify(response)


@api.route('/cars/<id>', methods = ['POST','PUT'])
@token_required
def update_car(current_user_token,id):
    car = Car.query.get(id) 
    car.make = request.json['make']
    car.year = request.json['year']
    car.model = request.json['model']
    car.features = request.json['features']
    car.user_token = current_user_token.token

    db.session.commit()
    response = contact_schema.dump(car)
    return jsonify(response)

@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()
    response = contact_schema.dump(car)
    return jsonify(response)