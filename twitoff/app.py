from flask import Flask, render_template, request
from .db_model import db, User
from .twitter import add_user_tweepy, update_all_users
from .predict import predict_user

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

    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])
    def add_or_update_user(name=None, message=''):
        name = name or request.values['user_name']

        try:
            if request.method == "POST":
                add_user_tweepy(name)
                message = "User {} successfully added!".format(name)
            tweets = User.query.filter(User.username == name).one().tweet
        except Exception as e:
            print(f'Error adding {name}: {e}')
            tweets = []
            
        return render_template('user.html', title=name, tweets=tweets, message=message)

    @app.route('/compare', methods=['POST'])
    def compare(message=''):
        user1 = request.values['user1']
        user2 = request.values['user2']
        tweet_text = request.values['tweet_text']

        if user1 == user2:
            message = 'Cannot compare a user to themelves'
        else:
            prediction = predict_user(user1, user2, tweet_text)

            message = f'''{tweet_text} is more likely to be said by 
                          {user1 if prediction else user2} than {user2 if prediction else user1}.'''

        return render_template('predict.html', title='Prediction', message=message)
    
    @app.route('/reset')
    def reset():
        db.drop_all()
        db.create_all()
        
    @app.route('/update', methods=['GET'])
    def update():
        update_all_users()
        return render_template('base.html', title='All Tweets Updated!', users=User.query.all())

    return app