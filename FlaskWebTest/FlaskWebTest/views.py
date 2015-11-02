﻿
from flask import Flask, render_template,request,redirect,flash,g,url_for
from flask.ext.sqlalchemy import SQLAlchemy

from flask import Flask, render_template,request,redirect,flash,g,url_for

#from forms import LoginForm
import forms
import datetime
import models

from app import app,db

@app.route('/')
@app.route("/index/",methods=['GET','POST'])
def index():
    #if g.user is not None and g.user.is_authenticated:
        #return redirect(url_for('index'))
    #flash("Users loaded successfully", "success")
    #flash("Welcome Home!", "success")
    #flash("Test flash messages!", "warning")
    users=models.User.query.all()
    
    return render_template('index.html',
                           title='Users list',users=users)

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.LoginForm()
    users=models.User.query.all()
    if form.validate_on_submit():
        flash("Yay, you registered!", "success")
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
    return render_template('login.html',
                           title='Login',
                           form=form,users=users)

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