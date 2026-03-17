from flask import Blueprint, request, jsonify, json
from werkzeug.security import check_password_hash, generate_password_hash
from .models import Users
from . import db
from flask_jwt_extended import jwt_required, create_access_token

auth = Blueprint('auth', __name__)

@auth.route("/register", methods=['POST'])
def register():

    if not request.is_json:
        return jsonify({"error": "request must be json"}), 415
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "no input"}), 400

    name = data.get('name')
    if not name:
        return jsonify({"error": "Please type a name"})
    password = data.get('password')
    if not password:
        return jsonify({"error": "please provide a password"})
    
    hashed_password = generate_password_hash(password)

    existing_username = Users.query.filter_by(name=name).first()
    if existing_username:
        return jsonify({"message": "name already exists"})

    user = Users(name=name, password=hashed_password)

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "registration completed",
        "user": user.to_dict()
        })



@auth.route("/login", methods=['POST'])
def login():
    
    data = request.get_json()

    name = data.get('name')
    password = data.get('password')
    if not name:
        return jsonify({"error": "please provide name"}), 400
    if not password:
        return jsonify({"error": "please provide password"}), 400

    user = Users.query.filter_by(name=name).first()
    if not user:
        return jsonify({"message": "user does not exist"}), 400
    
    if not check_password_hash(user.password, password):
        return jsonify({"message": "password incorrect"}), 400
    
    access_token = create_access_token(identity=str(user.id))
    
    return jsonify({
        "message": "login successful",
        "access_token": access_token
        }), 200
 
