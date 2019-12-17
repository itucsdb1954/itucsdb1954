from flask_wtf import FlaskForm,Form
from wtforms import StringField, PasswordField, TextField,SubmitField,validators
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])

    password = PasswordField("Password", validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = TextField('Username', validators=[DataRequired()],[validators.Length(min=4, max=20)])
    email = TextField('Email Address', validators=[DataRequired()],[validators.Length(min=6, max=50)])
    password = PasswordField('Password',validators=[DataRequired()], [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
