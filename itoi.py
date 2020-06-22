import os
from os import path
import re
import csv
import pandas
import numpy as np
import pandas as pd
from flask import Flask, request, url_for, Markup, redirect, render_template
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from forms import loginForm, signupForm

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

pswd = 'December9_$'
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:{}@localhost:3306/ITOI_DB'.format(pswd),echo=True)
Base = automap_base()
Base.prepare(engine, reflect=True)

@app.route('/', methods=['GET', 'POST'])
def login():
	form = loginForm()
	errors = []

	if form.validate_on_submit():
		data = form.data

		userID = data["userID"]
		pswd = data["pswd"]

		table = Base.classes.USER
		session = Session(engine)
		dbUserData = session.query(table).all()

		for row in dbUserData:
			if userID == row.USERNAME:
				if pswd == row.PASSWORD:
					return render_template('dashboard.html')
				else:
					message = "The password is incorrect. Please try again."
					return render_template('login.html', message=message, form=form)
			else:
				message = "This user does not exist. Please register"
				return render_template('login.html', message=message, form=form)
	
	return render_template('login.html', form = form)

@app.route('/SignUp', methods=['GET', 'POST'])
def userSignup():
	form = signupForm()
	errors = []

	if form.validate_on_submit():
		data = form.data
		userID = data["userID"]
		pswd = data["pswd"]
		isManager = data["isManager"]

		table = Base.classes.USER
		session = Session(engine)
		dbUserData = session.query(table).all()
		
		dbUsers = []
		for row in dbUserData:
			dbUsers.append(row.USERNAME)

		if userID in dbUsers:
			message = 'The user ID %s is already in use, choose another one' % userID
			return render_template('signup.html', message=message, form=form)
		else:
			userClass = Base.classes.USER
			newUser = userClass(USERNAME = userID, PASSWORD = pswd, IS_MANAGER = isManager)
			session.add(newUser)
			session.commit()
			message = 'The user has been registered. Please login to continue'
			return render_template('login.html', message=message, form=loginForm())

	return render_template('signup.html', form=form)


@app.route('/Dashboard', methods=['GET', 'POST'])
def landingPage():
	return render_template('dashboard.html')
