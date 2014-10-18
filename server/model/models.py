from server import db

instructions = db.Table('instructions',
	db.Column('drink_id', db.INTEGER, db.ForeignKey('drink.id')),
	db.Column('bottle_id', db.INTEGER, db.ForeignKey('bottle.id')),
	db.Column('amount', db.INTEGER)
)

class Drink(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    num = db.Column(db.INTEGER)
	inst = db.relationship('Instructions', secondary=instructions,
		backref=db.backref('drink

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
		
		
	