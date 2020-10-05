from flask import Flask, render_template, request
from .db_model import db, User

def create_app():
    '''
    Create and configure an instance of 
    the flask application
    '''

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/charliemay/Desktop/Lambda/DSPT7/DSPT7-Twitoff/twitoff/twitoff.sqlite" # using absolute filepath on Mac (recommended)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='Home', users=User.query.all())

    @app.route('/<username>/<followers>')
    def add_user(username, followers):
        user = User(username=username, followers=followers)
        DB.session.add(user)
        DB.session.commit()

        return f'{username} has been added to the DB!'

    return app