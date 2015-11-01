"""
The flask application package.
"""

from flask import Flask, render_template,request,redirect,flash,g,url_for
from flask.ext.sqlalchemy import SQLAlchemy

from flask import Flask, render_template,request,redirect,flash,g,url_for

#from forms import LoginForm,RegisterForm
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





@app.route('/')
@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegisterForm()
    users=models.User.query.all()
    if form.validate_on_submit():
        #flash("Yay, you registered!", "success")
        user=models.User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            joined_at=datetime.datetime.utcnow()
        )
        try:
            db.session.add(user)
            db.session.commit()
            flash("Yay, you registered!", "success")
        except Exception as e:
            raise

        return redirect(url_for('register'))
    return render_template('register.html',
                           title='Register',
                           form=form,users=users)

"""

if __name__ == '__main__':
    #db.create_all()
    app.run(debug=DEBUG, host=HOST, port=PORT)


from os import environ

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    #db.create_all()
    app.run(HOST, PORT)
"""