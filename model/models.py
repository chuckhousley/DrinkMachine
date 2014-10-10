import drinkDB

class Drink(drinkDB.db.Model):
    id = drinkDB.db.Column(db.INTEGER, primary_key=True)
    name = drinkDB.db.Column(db.TEXT)
    num = drinkDB.db.Column(db.INTEGER)

    def __init__(self, name):
        self.name = name
        self.num = 0

    def __repr__(self):
        return self.name

