from flask_wtf import FlaskForm, Form
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, IntegerField, TextAreaField, DateTimeField, BooleanField, SelectField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Optional

class loginForm(FlaskForm):
	userID = StringField('Enter User ID:', validators=[DataRequired()])
	pswd = PasswordField('Enter password:', validators=[DataRequired()])
	submit = SubmitField('Login')

class signupForm(FlaskForm):
	userID = StringField('Enter User ID', validators=[DataRequired()])
	pswd = PasswordField('Enter password:', validators=[DataRequired()])
	isManager = BooleanField("Is Manager?")
	submit = SubmitField('Register')