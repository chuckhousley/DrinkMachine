from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager
from server import app
# import server.model.models

db = SQLAlchemy(app)
# api_manager = APIManager(app, flask_sqlalchemy_db=db)
# api_manager.create_api(model.models.Drink, methods=['GET'])
