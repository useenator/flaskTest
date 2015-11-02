"""
The flask application package.
"""

from flask import Flask, render_template,request,redirect,flash,g,url_for
from flask.ext.sqlalchemy import SQLAlchemy

from flask import Flask, render_template,request,redirect,flash,g,url_for


import forms
import datetime
import models


"""
DEBUG = True
HOST = "127.0.0.1"
PORT = 5000
"""
app = Flask(__name__)
app.secret_key='secret_key'

#from flask.ext.sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


from views import *


from os import environ

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    #db.create_all()
    app.run(HOST, PORT)
