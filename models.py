import sqlite3 as db

_conn = db.connect('drink.db', check_same_thread=False)
_conn.row_factory = db.Row
_cursor = _conn.cursor()


class DrinkModel:
    def __init__(self):
        pass

    @classmethod
    def add_drink(cls, name):
        _cursor.execute('INSERT INTO drink(text) VALUES(?)', (name, ))
        _conn.commit()

