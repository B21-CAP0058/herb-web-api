import os
import pymysql
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(object):
    DEBUG = False
    JSON_SORT_KEYS = False
    DB_HOST = os.environ.get('DB_HOST') 
    DB_USER = os.environ.get('DB_USER') 
    DB_PASS = os.environ.get('DB_PASS')
    DB_NAME = os.environ.get('DB_NAME')
    DB_INSTANCE = os.environ.get('DB_INSTANCE')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(DB_USER,DB_PASS,DB_HOST,DB_NAME) 
    #SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://{nam}:{pas}@/{dbn}?unix_socket=/cloudsql/{con}'.format(nam=DB_USER,pas=DB_PASS,dbn=DB_NAME,con=DB_INSTANCE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
