from flask import Flask
import logging
from flask_cache import Cache
from flask_sqlalchemy import SQLAlchemy
from aggregator import Aggregator

app = Flask('application', instance_relative_config=True)

# app.config.from_object('config.ProductionConfig')
app.config.from_object('config.DevelopmentConfig')
app.config.from_pyfile('application.cfg')
app.config['SQLALCHEMY_DATABASE_URI']=app.config['SQLALCHEMY_DATABASE_URI_TEMPLATE'].format(app.config['SQLALCHEMY_DATABASE_USER'],
                                                                                            app.config['SQLALCHEMY_DATABASE_PASSWORD'],
                                                                                            app.config['SQLALCHEMY_DATABASE_DB_NAME'])

# db = SQLAlchemy(app)

# cache = Cache(app, config={'CACHE_TYPE': 'simple'})
# cache.init_app(app)

agg = Aggregator()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import views
