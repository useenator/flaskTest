'''
from flask import Flask, render_template,request,redirect,flash,g,url_for
from flask.ext.sqlalchemy import SQLAlchemy

from flask import Flask, render_template,request,redirect,flash,g,url_for

from forms import LoginForm,RegisterForm
#import forms
import datetime
import models

from appp import app,db
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

'''