from flask import Flask
import logging
from flask_cache import Cache
from flask_sqlalchemy import SQLAlchemy
from aggregator import Aggregator
from flask_pymongo import PyMongo



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = Flask('application', instance_relative_config=True)

# app.config.from_object('config.ProductionConfig')
app.config.from_object('config.DevelopmentConfig')
try:
    app.config.from_pyfile('application.cfg')
except IOError:
    logger.info('no instance config foud')

mongo = PyMongo(app)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cache.init_app(app)
agg = Aggregator()

import views
