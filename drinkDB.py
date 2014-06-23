import sqlite3 as db
from flask import g

def connect_db():
    conn = db.connect('drink.db')
    conn.row_factory = db.Row
    return conn

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
