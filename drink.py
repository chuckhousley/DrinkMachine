# -*- coding: utf-8 -*-
import os
from server import app, db
import server.model


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)  # host='10.10.56.190')


