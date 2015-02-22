from flask import render_template, request, redirect, url_for
from flask.views import MethodView
import json
from server import app, db
from server.model.models import Drink, Bottle

@app.route('/')
def display_start():
    drinks = Drink.query.all()
    bottles = Bottle.query.all()
    return render_template('main.html', drinks=drinks, bottles=bottles)

@app.route('/add', methods=['POST'])
def add_drink():
    if request.method == 'POST':
        drink = Drink(request.form['drink_name'])
        db.session.add(drink)
        db.session.commit()
        # get everything else
        return redirect(url_for('display_start'))


        ###### database functions below ######
@app.route('/add_bottle', methods=['POST'])
def add_bottle():
    if request.method == 'POST':
        bottle = Bottle(request.form['bottle'], request.form['amount'])
        db.session.add(bottle)
        db.session.commit()
        return redirect(url_for('display_start'))
    
def delete_bottle(name):
    bottle = Bottle.query.filter_by(name).first()
    if bottle:
        db.session.delete(bottle)
    
    
def add_to_machine(bottle_id, position):
    pos = Machine.query.filter_by(position).first()
    if (pos is None):
        machine = Machine(position, bottle_id)
        db.session.add(machine)
        db.session.commit()
        
    else:
        pos.bottle = bottle_id
        db.session.commit()


def _add_drink(name, instructions):
    drink = Drink(name)
    db.session.add(drink)
    for i in instructions:
        db.session.add(i)
    db.session.commit()