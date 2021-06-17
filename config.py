import os
class Config:
    '''
    General configuration parent class
    '''
    pass


    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:access@localhost/myprofile'
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
            
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://",1)


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}