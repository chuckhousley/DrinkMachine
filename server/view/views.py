from flask import render_template
from flask.views import MethodView
import json
from server import app
from server.model.models import Drink

@app.route('/')
def display_start():
    drinks = Drink.query.all()
    return render_template('main.html', drinks=drinks)

@app.route('/add', methods=['POST'])
def add_drink():
    drink_name = request.form['drink_name']
    # get everything else

