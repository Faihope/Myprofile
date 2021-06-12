from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Email, EqualTo,Length,Email,EqualTo

class RegistrationForm():
    username = StringField('username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('email',validators[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up')