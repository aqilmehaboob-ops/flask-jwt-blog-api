# Flask REST API with JWT Authentication

## 🚀 Overview

This project is a REST API built using Flask. It includes user authentication, authorization, and CRUD operations for posts.

---

## 🔐 Features

* User Registration & Login (JWT Authentication)
* Password Hashing for Security
* Protected Routes using JWT
* Authorization (users can only modify their own data)
* CRUD operations for Posts
* User-specific endpoints (`/users/me`)
* SQLAlchemy Relationships

---

## 🛠 Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* Flask-JWT-Extended
* SQLite

---

## 📌 API Endpoints

### Authentication

* `POST /register` → Register new user
* `POST /login` → Login and get JWT token

### Users

* `GET /users` → Get all users
* `GET /users/me` → Get current user
* `PUT /users` → Update current user
* `DELETE /users` → Delete current user

### Posts

* `POST /users/posts` → Create post
* `GET /users/posts` → Get all posts
* `GET /users/<user_id>/posts` → Get posts of specific user
* `GET /users/posts/<post_id>` → Get single post
* `PUT /users/posts/<post_id>` → Update post (owner only)
* `DELETE /users/posts/<post_id>` → Delete post (owner only)

---

## ⚙️ Installation

```bash
git clone https://github.com/aqilmehaboob-ops/flask-jwt-blog-api.git
cd Flask rest api project
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python run.py
```

---

## 🔑 Authentication

After login, include this header in requests:

```
Authorization: Bearer <your_token>
```

---

## 📚 What I Learned

* REST API design
* JWT authentication and authorization
* Database relationships using SQLAlchemy
* Secure backend development practices
* Clean project structure using Flask Blueprints
