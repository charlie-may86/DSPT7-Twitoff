from flask import Flask, render_template
from .db_model import db

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
        return render_template('base.html')

    return app