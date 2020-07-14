from flask_wtf import FlaskForm, Form
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, IntegerField, TextAreaField, DateTimeField, BooleanField, SelectField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Optional

class loginForm(FlaskForm):
	mngrID = StringField('Enter User ID:', validators=[DataRequired()])
	pswd = PasswordField('Enter password:', validators=[DataRequired()])
	key = StringField('Enter Org Key', validators=[DataRequired()])
	submit = SubmitField('Login')

class signupForm(FlaskForm):
	mngrID = StringField('Enter Manager ID', validators=[DataRequired()])
	pswd = PasswordField('Enter password:', validators=[DataRequired()])
	cpswd = PasswordField('Confirm password:', validators=[DataRequired()])
	emailID = StringField('Enter Email ID', validators=[DataRequired()])
	key = StringField('Enter Org Key', validators=[DataRequired()])
	submit = SubmitField('Register')