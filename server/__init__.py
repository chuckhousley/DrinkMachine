# -*- coding: utf-8 -*-
import os
from flask import Flask, request, render_template
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drink.db'
app.debug = True
from controllers import *
