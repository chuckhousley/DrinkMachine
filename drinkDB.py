from flask.ext.restless import APIManager


def init_db(app, db):
    class Drink(db.Model):
        id = db.Column(db.INTEGER, primary_key=True)
        name = db.Column(db.TEXT)
        num = db.Column(db.INTEGER)

    db.create_all()

    api_manager = APIManager(app, flask_sqlalchemy_db=db)
    api_manager.create_api(Drink, methods=['GET', 'POST', 'DELETE', 'PUT'])