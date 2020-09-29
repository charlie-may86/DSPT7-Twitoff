from flask import Flask

# __name__ references the name of the file, in this case
# hello.py
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About me...'
