from .models import Posts, Users
from flask import Blueprint, request, jsonify
from . import db
from flask_jwt_extended import jwt_required, get_jwt_identity

posts = Blueprint("posts", __name__)

@posts.route("/users/posts", methods=['POST'])
@jwt_required()
def createpost():

    current_user = get_jwt_identity()

    if not request.is_json:
        return jsonify({"error": "request must be in json"}), 400

    data = request.get_json()
    title = data.get('title')
    if not title:
        return jsonify({"error": "please provide title"}), 400

    post = Posts(title=title, user_id=current_user)

    db.session.add(post)
    db.session.commit()

    return jsonify(post.to_dict()), 201



@posts.route("/users/posts", methods=['GET'])
@jwt_required()
def allposts():

    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 5, type=int)
    offset = (page - 1) * limit

    posts = Posts.query.offset(offset).limit(limit).all()
    
    return jsonify([post.to_dict() for post in posts]), 200


@posts.route("/users/<int:user_id>/posts", methods=['GET'])
@jwt_required()
def userposts(user_id):

    user = Users.query.get_or_404(user_id)
    posts = user.posts
    
    return jsonify([post.to_dict() for post in posts]), 200

    
@posts.route("/users/posts/<int:post_id>", methods=['GET'])
@jwt_required()
def oneposts(post_id):

    post = Posts.query.get_or_404(post_id)

    return jsonify(post.to_dict()), 200

@posts.route("/users/posts/<int:post_id>", methods=['PUT'])
@jwt_required()
def updateposts(post_id):

    current_user = get_jwt_identity()

    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"error": "title is required"}), 400

    post = Posts.query.filter_by(user_id=current_user, id=post_id).first_or_404()

    post.title = data.get('title')

    db.session.commit()

    return jsonify({
        "message": "title_updated",
        "new_title": post.title
    }), 200


@posts.route("/users/posts/<int:post_id>", methods=['DELETE'])
@jwt_required()
def deletepost(post_id):

    current_user = get_jwt_identity()

    post = Posts.query.filter_by(user_id=current_user, id=post_id).first_or_404()

    db.session.delete(post)
    db.session.commit()

    return jsonify({
        "message": "post deleted",
        "user": post.to_dict()
    }), 200
