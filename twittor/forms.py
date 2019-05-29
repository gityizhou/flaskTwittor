from flask_wtf import FlaskForm
# import wtfforms field
from wtforms import StringField, PasswordField, BooleanField, SubmitField
# import validator, Flask uses the WTForms module to validate Post Requests
from wtforms.validators import DataRequired

# three parts of form
# 1 the form class
# 2 the template containing the form
# 3 the route for processing the form


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Log in")