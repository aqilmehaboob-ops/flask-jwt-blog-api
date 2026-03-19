from . import db

class Users(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(300))

    posts = db.relationship("Posts", backref="author", cascade="all, delete")

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name
        }



class Posts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def to_dict(self):
        return{
            "post_id": self.id,
            "title": self.title,
            "user_id": self.user_id
        }
