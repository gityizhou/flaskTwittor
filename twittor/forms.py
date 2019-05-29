from flask_wtf import FlaskForm
# import wtfforms field
from wtforms import StringField, PasswordField, BooleanField, SubmitField
# import validator, Flask uses the WTForms module to validate Post Requests
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from twittor.models import User
# three parts of form
# 1 the form class
# 2 the template containing the form
# 3 the route for processing the form


class LoginForm(FlaskForm):

    class Meta:
        csrf = False

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Log in")


class RegisterForm(FlaskForm):

    class Meta:
        csrf = False

    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Password Repeat", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("submit")

    def validate_username(self, username):   # 检查username是否重复
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('existed username')

    def validate_email(self, email):  # 检查email是否重复
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('existed email')