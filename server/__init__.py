# -*- coding: utf-8 -*-
import os
from flask import Flask, request, jsonify, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drink.db'
db = SQLAlchemy(app)
# api_manager = APIManager(app, flask_sqlalchemy_db=db)
# api_manager.create_api(model.models.Drink, methods=['GET'])
import server.model.models as model

