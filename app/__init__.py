from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    jwt = JWTManager()
    jwt.init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogs.db'
    app.config["JWT_SECRET_KEY"] = "super-secret"

    db.init_app(app)

    from .users_route import users
    from .auth_route import auth
    from .posts_route import posts
    
    app.register_blueprint(posts)
    app.register_blueprint(auth)
    app.register_blueprint(users)

    return app







