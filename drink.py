# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Chuck Housley
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
"""

import os
from flask import Flask, request, session, g, render_template
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy

# create application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drink.db'
db = SQLAlchemy(app)


class Drink(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    num = db.Column(db.INTEGER)

db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Drink, methods=['GET', 'POST', 'DELETE', 'PUT'])


@app.route('/')
def hello():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)  # host='10.10.56.190')


