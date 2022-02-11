from distutils.log import DEBUG


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/pickmenow'
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True