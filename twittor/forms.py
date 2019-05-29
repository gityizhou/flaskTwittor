from flask_wtf import FlaskForm
# import wtfforms field
from wtforms import StringField, PasswordField, BooleanField, SubmitField
# import validator
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Log in")