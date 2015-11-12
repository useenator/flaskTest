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

#Upload config
import os

#APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#UPLOAD_FOLDER = os.path.join(APP_ROOT, '/uploads')
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#UPLOAD_FOLDER = r"E:\Documents\Visual Studio 2015\Projects\FlaskWebTest\FlaskWebTest\FlaskWebTest\uploads"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#app = Flask(__name__)

app.config.from_object(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from upload import *

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
