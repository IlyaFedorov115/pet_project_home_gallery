import os

class Config(object):

    APPNAME = 'app'
    ROOT = os.path.abspath(APPNAME) # /home/git/pet...
    UPLOAD_PATH = '/static/upload/'
    SERVER_PATH = ROOT + UPLOAD_PATH

    USER = os.environ.get('POSTGRES_USER', 'pet_role')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'pet_role')
    HOST = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT = os.environ.get('POSTGRES_PORT', 5432)
    DB = os.environ.get('POSTGRES_DB', 'pet_db')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SECRET_KEY = 'fdfjkgdfjgkdfjg454ewrt'
    SQLALCHEMY_TRACK_MODIFICATIONS = True