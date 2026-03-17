from flask import Blueprint, jsonify, request
from .models import Users
from . import db
from flask_jwt_extended import jwt_required, get_jwt_identity

users = Blueprint('users', __name__)

@users.route("/users", methods=['GET'])
def all_users():

    result = []

    all_user = Users.query.all()

    for user in all_user:
        result.append({
            "userid": user.id,
            "username": user.name
        })

    return jsonify(result), 200


@users.route("/users/me", methods=['GET'])
@jwt_required()
def oneuser():

    current_user = get_jwt_identity()

    user = Users.query.get_or_404(current_user)

    return  jsonify(user.to_dict()), 200


@users.route("/users", methods=['PUT'])
@jwt_required()
def updateuser():

    current_user = get_jwt_identity()
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "no input"}), 400

    user = Users.query.filter_by(id=current_user).first_or_404()

    name = data.get('name')
    if not name:
        return {"error": "name is required"}, 400  
    user.name = name

    db.session.commit()

    return jsonify({"message": "user updated"}), 200


@users.route("/users", methods=['DELETE'])
@jwt_required()
def deleteuser():

    current_user = get_jwt_identity()
    
    user = Users.query.get_or_404(current_user)

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "user deleted"}), 200



