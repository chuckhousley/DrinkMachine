Drink machine
=============

from the very top:
* apt-get update
* apt-get upgrade
* apt-get install build-essentials python-dev nginx sqlite3
* apt-get install python-pip
* if apt doesn't get pip for whatever reason:
  * wget http://pypi.python.org/packages/source/p/pip/pip-1.5.tar.gz
  * tar xzf pip-1.5.tar.gz
  * cd pip-1.5
  * python setup.py install
* pip install Flask
* pip install uwsgi
* pip install Flask-Restless
* pip install Flask-SQLAlchemy

