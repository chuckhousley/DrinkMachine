from flask import request, jsonify, render_template
from models import DrinkModel
import flask.views
import json


class DrinkView(flask.views.MethodView):
    def get(self):
        return render_template('main.html')

