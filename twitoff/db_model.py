'''
SQLAlchemy model for twitoff
'''
from flask_sqlalchemy import SQLAlchemy

#This code is creating the database structure

#instaniate SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    follower_count  = db.Column(db.String(120), nullable=False)

    # this is called a dunder method
    def __repr__(self):
        return '<User %r>' % self.username

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Unicode(300))
    user = db.relationship('User', backref=db.backref('tweet', lazy=True))

    # this is called a dunder method
    def __repr__(self):
        return '<Tweet %r>' % self.text

