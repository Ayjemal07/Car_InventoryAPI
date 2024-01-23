import os
from dotenv import load_dotenv,find_dotenv
basedir = os.path.abspath(os.path.dirname(__name__))
# load_dotenv(os.path.join(basedir, '.env'))

load_dotenv(find_dotenv())
class Myconfig():
    '''
        Set config variables for the flask app
        Using Environment variables where available.
        Otherwise create the config variable if not done already
    '''

    x=1
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_NOTIFICAITONS = False
