import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    ADMIN_EMAIL = "canjian.myself@gmail.com"

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = ''
    APP_NAME = 'Late Night Show Aggregator'

    LISTINGS_PER_PAGE = 5

    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_CONFIRMABLE = True


    # SendGrid example.
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True

    # channel ids
    CHANNELIDS=['UCwWhs_6x42TyRM4Wstoq8HA',
                'UCMtFAi84ehTSYSE9XoHefig',
                'UC3XTzVzaHQEd30rQbuvCtTQ',
                'UCVTyTA7-g9nopHeHbeuvpRA'
    ]
    
    MONGO_HOST=os.environ.get('MONGO_HOST')
    MONGO_PORT=os.environ.get('MONGO_PORT')
    MONGO_DBNAME=os.environ.get('MONGO_DBNAME')
    MONGO_USERNAME=os.environ.get('MONGO_USERNAME')
    MONGO_PASSWORD=os.environ.get('MONGO_PASSWORD')

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
