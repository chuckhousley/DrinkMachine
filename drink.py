# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Chuck Housley
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
"""

import os
from server import app

if __name__ == "__main__":
    app.run(debug=True)  # host='10.10.56.190')


