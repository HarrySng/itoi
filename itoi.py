import os
from os import path
import re
import csv
import pandas
import numpy as np
import pandas as pd
from flask import Flask, request, url_for, Markup, redirect, render_template
from forms import loginForm, signupForm
from logic import *
from parentLogic import *

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def orgPage():
	orgs = getOrgs()
	return render_template('org.html', orgs = orgs)

@app.route('/login', methods=['GET', 'POST'])
def login():
	orgName = request.form.get('orgs') # Return the org selected by user
	orgID = db.session.query(classDict['ORG']).filter(classDict['ORG'].ORG_NAME == orgName)[0].ID
	
	form = signupForm()
	errors = []
	
	if form.validate_on_submit():
		data = form.data
		mngrID = data['mngrID']
		pswd = data['pswd']
		key = data['key']
		# Check if manager ID or email already exists in org
		qManager = db.session.query(classDict['MANAGER']).filter(classDict['MANAGER'].ORG_ID == orgID)
		mngrIDs = []
		for row in qManager:
			mngrIDs.append(row.USERNAME)
			keys.append(row.ORG_KEY)
		if mngrID not in mngrIDs:
			errors.append("This manager ID does not exist in this organization.")
			return render_template('generic_text.html', error=Markup("<br/>".join(errors)))
		
		# Check key
		orgKey = db.session.query(orgClass).filter(orgClass.ORG_ID == orgID)[0].ORG_KEY
		if key != orgKey:
			errors.append("The key does not match the organization key.")
			return render_template('generic_text.html', error=Markup("<br/>".join(errors)))

		# Check pswd
		truepswd = db.session.query(classDict['MANAGER']).filter(classDict['MANAGER'].ORG_ID == orgID).filter(classDict['MANAGER'].USERNAME == mngrID)[0].PASSWORD
		if pswd != truepswd:
			errors.append("The password is incorrect.")
			return render_template('generic_text.html', error=Markup("<br/>".join(errors)))

		# If all checks pass
		# run a dashboard function thatn pulls all info of this user and then push it to dashboard.html
		# Example:
		results = getDashboard(orgID, mngrID)
		
		return render_template('dashboard.html')

	return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	orgName = request.form.get('orgs') # Return the org selected by user
	orgID = db.session.query(classDict['ORG']).filter(classDict['ORG'].ORG_NAME == orgName)[0].ID
	
	form = signupForm()
	errors = []
	
	if form.validate_on_submit():
		data = form.data
		mngrID = data['mngrID']
		pswd = data['pswd']
		cpswd = data['cpswd']
		email = data['email']
		key = data['key']
		# Check if manager ID or email already exists in org
		qManager = db.session.query(classDict['MANAGER']).filter(classDict['MANAGER'].ORG_ID == orgID)
		mngrIDs = []
		emailIDs = []
		for row in qManager:
			mngrIDs.append(row.USERNAME)
			emailIDs.append(row.EMAIL_ID)
			keys.append(row.ORG_KEY)
		if mngrID in mngrIDs:
			errors.append("This manager ID already exists in this organization.")
			return render_template('generic_text.html', error=Markup("<br/>".join(errors)))
		if email in emailIDs:
			errors.append("This email ID already exists in this organization.")
			return render_template('generic_text.html', error=Markup("<br/>".join(errors)))
		
		# Check key
		orgKey = db.session.query(orgClass).filter(orgClass.ORG_ID == orgID)[0].ORG_KEY
		if key != orgKey:
			errors.append("The key does not match the organization key.")
			return render_template('generic_text.html', error=Markup("<br/>".join(errors)))

		# Check if password and confirm password fields match
		if pswd != cpswd:
			errors.append("The passwords do not match. Please try again.")
			return render_template('generic_text.html', error=Markup("<br/>".join(errors)))

		# If all checks pass, insert SQL
		manager.addManager(userName = mngrID, pswd = pswd, email = email, orgID = orgID)

		errors.append("Manager is Registered! Please login.") # Reuse errors page for successful registration also
		return render_template('generic_text.html', error=Markup("<br/>".join(errors)))

	return render_template('signup.html', form=form)
