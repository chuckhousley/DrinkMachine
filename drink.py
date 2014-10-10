# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Chuck Housley
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
"""

import os
from flask import Flask, request, session, g, render_template
from drinkDB import init_db
from flask.ext.sqlalchemy import SQLAlchemy

# create application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drink.db'
db = SQLAlchemy(app)

init_db(app, db)


@app.route('/_get_drinks')
def get_drinks():
    pass


@app.route('/')
def hello():
    drinks = []
    return render_template('main.html', drinks=drinks)


if __name__ == "__main__":
    app.run(debug=True)  # host='10.10.56.190')


