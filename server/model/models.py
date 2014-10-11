from server import db

class Drink(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    num = db.Column(db.INTEGER)

    def __init__(self, name):
        self.name = name
        self.num = 0

    def __repr__(self):
        return self.name

