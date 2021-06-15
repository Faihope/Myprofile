from . import db
from . import login_manager
from flask_login import UserMixin
from datetime import datetime

from werkzeug.security import generate_password_hash,check_password_hash
class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    # posts_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    post = db.relationship('Post',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    def __repr__(self):
        return f"User('{self.username}')"

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # users = db.relationship('User',backref = 'posts',lazy="dynamic")
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_post(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_posts(cls,id):
        posts = Post.query.filter_by(id=id).all()
        return posts

    def __repr__(self):
        
        return f"Post('{self.title}', '{self.posted_date}', '{self.category}')"
    
    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)
    posted_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,id):
        comments = Comment.query.filter_by(post_id=id).all()
        return comments
    
    def __repr__(self):
        return f"Comment('{self.comment}', '{self.posted_date}')"
