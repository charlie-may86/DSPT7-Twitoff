# DSPT7-Twitoff
A fun python web application for comparing and predicting Tweet authorship.

# To run hello.py
```sh
FLASK_APP=hello.py flask run
```

# To run app.py
```sh
FLASK_APP=twitoff flask run
```

# To run twitoff app and get an interactive enviroment to play around
```sh
FLASK_APP=twitoff:APP flask shell
```
# To create database
```sh
from twitoff.db_model import db, User, Tweet
db.create_all()
u1 = User(username='austen', follower_count=135000)
db.session.add(u1)
db.session.commit()
```

# To reset database
```sh
db.drop_all()
db.create_all()
```

# To add a tweet and user in the same session
```sh
tweet1 = Tweet(tweet='try this', user=u1)
db.session.add(tweet1)
db.session.commit()
```
The user and tweet must be made in the same session to add users in this way. If they are not made in the same session, the tweet cannot be associated with a user.

# To add a tweet with a user made in a previous session
```sh
t1 = Tweet(tweet='text', user=User.query.filter_by(username='user').first())
db.session.add(tweet1)
db.session.commit()
```
# return all users
```sh
User.query.all()
```

# reference page for flask-sql alchemy
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/ 

# To update heroku app
```sp
git push heroku master
```