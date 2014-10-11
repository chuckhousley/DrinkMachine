from flask import render_template
from flask.views import MethodView
import json
from server import app
from server.model.models import Drink

@app.route('/')
def display_start():
    drinks = Drink.query.all()
    return render_template('main.html', drinks=drinks)

class DrinkView(MethodView):
    def get(self):
        drinks = None

    def put(self):
        pass


app.add_url_rule('/', view_func=DrinkView.as_view('display_front'))

