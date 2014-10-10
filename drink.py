# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Chuck Housley
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
"""

import os
from flask import Flask, request, session, g, render_template

import drinkDB
import views


# create application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drink.db'
drinkDB.init_db(app)


@app.route('/_get_drinks')
def get_drinks():
    pass


@app.route('/')
def hello():
    views.DrinkView.get()


if __name__ == "__main__":
    app.run(debug=True)  # host='10.10.56.190')


