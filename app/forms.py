from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Email, EqualTo,Length,Email,EqualTo

class RegistrationForm():
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up')
    
class LoginForm():
   
    email = StringField('Email',validators[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remamber =BooleanField('Remember me')
    submit = SubmitField('Login')