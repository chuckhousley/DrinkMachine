# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Chuck Housley
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
"""

import os
import drinkDB
from views import DrinkView
from flask import Flask, request, session, g

# create application
app = Flask(__name__)
app.config.from_object(__name__)

# load up a config
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'drink.db'),
    DEBUG=True,
    SECRET_KEY='change this sometime',
    USERNAME='admin',
    PASSWORD='admin'
    ))
app.config.from_envvar('DRINK_SETTINGS', silent=True)

app.add_url_rule('/', view_func=DrinkView.as_view('drink_view'))

if __name__ == "__main__":
    app.run(host='10.10.56.190')


