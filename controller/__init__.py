from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager
from drink-machine import app
import model.models

db = SQLAlchemy(app)
api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(models.Drink, methods=['GET'])
