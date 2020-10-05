'''
SQLAlchemy model for twitoff
'''
from flask_sqlalchemy import SQLAlchemy

#This code is creating the database structure

#instaniate SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    follower_count  = db.Column(db.String(120), nullable=False)

    # this is called a dunder method
    def __repr__(self):
        return '<User %r>' % self.username

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(300), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tweet', lazy=True))
    
    # this is called a dunder method
    def __repr__(self):
        return '<Tweet %r>' % self.tweet

