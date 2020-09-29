'''Entry point to the twitoff flask application'''

from .app import create_app

# this is a clobal variable
APP = create_app()