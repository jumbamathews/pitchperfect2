import os


class Config:

    '''
    General configuration parent class
    '''
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevone:12345@localhost/pitchgoal'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #  email configurations
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
    SQLALCHEMY_DATABASE_URI =os.environ.get("HEROKU_POSTGRESQL_SILVER_URL")
    pass


class DevConfig(Config):

    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    DEBUG = True


CONFIG_OPTIONS = {
    'development': DevConfig,
    'production': ProdConfig
}
