from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager


db = None
def init_db(app):
    db = SQLAlchemy(app)
    db.create_all()
    api_manager = APIManager(app, flask_sqlalchemy_db=db)
    api_manager.create_api(models.Drink, methods=['GET', 'SET', 'PUT', 'DELETE'])


