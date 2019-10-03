from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class SignupForm(FlaskForm):
    name = StringField("Name", [validators.required(), validators.Length(min=2)])
    username = StringField("Username", [validators.Length(min=2)])
    password = PasswordField("Password", [validators.Length(min=2)])
    password2 = PasswordField("Password", [validators.Length(min=2)])

    class Meta:
        crsf = False


class ChangePasswordForm(FlaskForm):
    oldpassword = PasswordField("old password")
    password = PasswordField("new password")
    password2 = PasswordField("repeat new password")

    class Meta:
        crsf = False
