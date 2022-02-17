import os
class Config:

    #database uri from .env file

    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATION = False

    #account/profile image storage

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #account/profile image storage end

    
class ProdConfig(Config):
    pass
class DevConfig(Config):

    #database uri from .env file

    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATION = False

    
    DEBUG = True