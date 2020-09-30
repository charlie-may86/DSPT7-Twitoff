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



# reference page for flask-sql alchemy
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/ 