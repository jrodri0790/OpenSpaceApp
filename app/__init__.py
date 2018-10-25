import os

from flask import Flask
from flask_heroku import Heroku
from sqlalchemy_utils import database_exists, create_database, drop_database

from controllers.vote_controller import vote_blueprint
from database.database import db

app = Flask(__name__)
ENVIRONMENT_DEBUG = os.environ.get("ENV", default='development')
if ENVIRONMENT_DEBUG == 'development':
    app.logger.debug('Entra al if de development')
    app.debug = True
    DB_URL = 'postgresql://postgres:mysecretpassword@localhost:5432/mybase'
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    with app.app_context():
        db.init_app(app)
        app.logger.debug("before delete database")
        if database_exists(DB_URL):
            app.logger.debug('Deleting database.')
            drop_database(DB_URL)
        if not database_exists(DB_URL):
            app.logger.debug('Creating database.')
            create_database(DB_URL)
        app.logger.debug('Creating tables.')
        app.logger.debug("before create")
        try:
            db.create_all()
        except BaseException as e:
            app.logger.debug(e)
        app.logger.debug('Shiny!')
else:
    app.debug = False
    heroku = Heroku(app)
    with app.app_context():
        db.init_app(app)
        app.logger.warning('Creating tables. heroku')
        db.create_all()
        app.logger.warning('Shiny! heroku')

app.register_blueprint(vote_blueprint, url_prefix=f'/open-space')