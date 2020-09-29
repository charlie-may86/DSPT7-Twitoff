from flask import Flask

# __name__ references the name of the file, in this case
# hello.py

def create_app():
    '''
    Create and configure an instance of 
    the flask application
    '''

    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff!'

    return app