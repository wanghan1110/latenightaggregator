from flask import Flask
import logging
from flask_cache import Cache
from flask_sqlalchemy import SQLAlchemy
from aggregator import Aggregator

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


app = Flask('application', instance_relative_config=True)

# app.config.from_object('config.ProductionConfig')
app.config.from_object('config.DevelopmentConfig')
try:
    app.config.from_pyfile('application.cfg')
    app.config['SQLALCHEMY_DATABASE_URI']=app.config['SQLALCHEMY_DATABASE_URI_TEMPLATE'].format(app.config['SQLALCHEMY_DATABASE_USER'],
                                                                                            app.config['SQLALCHEMY_DATABASE_PASSWORD'],
                                                                                            app.config['SQLALCHEMY_DATABASE_DB_NAME'])
except IOError:
    logger.info('no instance config foud')

# db = SQLAlchemy(app)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cache.init_app(app)
agg = Aggregator()

import views
