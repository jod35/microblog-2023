from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class LoginForm(FlaskForm):
    username = StringField(label="username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    remember_me = BooleanField(label="remember me")
    submit = SubmitField("Sign In")
