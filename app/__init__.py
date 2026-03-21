from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    jwt = JWTManager()

    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    jwt.init_app(app)
    db.init_app(app)

    from .users_route import users
    from .auth_route import auth
    from .posts_route import posts
    
    app.register_blueprint(posts)
    app.register_blueprint(auth)
    app.register_blueprint(users)

    @app.route("/")
    def home():
        return {"message": "API is running"}

    return app







