from server import db

class Instructions(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    drink_id = db.Column(db.INTEGER, db.ForeignKey('drink.id'), nullable=False)
    bottle_id = db.Column(db.INTEGER, db.ForeignKey('bottle.id'), nullable=False)
    amount = db.Column(db.INTEGER, nullable=False)


class Drink(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    num = db.Column(db.INTEGER)
    inst = db.relationship('Bottle', secondary=instructions)

    
    def __init__(self, name):
        self.name = name
        self.num = 0

    def __repr__(self):
        return self.name


class Bottle(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    amount = db.Column(db.INTEGER)
    
    
    def __init__(self, amount):
        self.name = name
        self.amount = amount
        
    def __repr__(self):
        return self
        
        
class Machine(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    bottle = db.Column(db.INTEGER, db.ForeignKey('bottle.id'), unique=True)
    