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


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI_TEMPLATE = 'mysql://{}:{}@server_ip:server_port/{}'
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI_TEMPLATE = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI_TEMPLATE = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    TESTING = True
