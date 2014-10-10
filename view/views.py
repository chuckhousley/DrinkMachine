from flask import request, jsonify, render_template
from models import Drink
import flask.views
import json


class DrinkView(flask.views.MethodView):
    def get(self):
        drinks = Drink.query.all()
        return render_template('main.html', drinks=drinks)

