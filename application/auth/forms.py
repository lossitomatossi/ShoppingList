from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.validators import ValidationError, InputRequired, EqualTo, Length, DataRequired
from application.utils.errormessages import msg_username_length, msg_password_match, msg_password_length, msg_name_length

class LoginForm(FlaskForm):
    username = StringField("Username", [InputRequired(), Length(min=1, max=144, message=msg_username_length), DataRequired(message="Only using spaces not allowed")])
    password = PasswordField("Password", [InputRequired(), Length(min=1, max=144, message=msg_password_length), DataRequired(message="Only using spaces not allowed")])

    class Meta:
        csrf = False


class SignupForm(FlaskForm):
    name = StringField("Name", [InputRequired(), Length(min=1, max=144, message=msg_name_length), DataRequired(message="Only using spaces not allowed")])
    username = StringField("Username", [InputRequired(), Length(min=1, max=144, message=msg_username_length),DataRequired(message="Only using spaces not allowed")])
    password = PasswordField("Password", [validators.required(), validators.Length(min=2), DataRequired(message="Only using spaces not allowed")])
    password2 = PasswordField("Password", [validators.required(), validators.Length(min=2), DataRequired(message="Only using spaces not allowed")])

    class Meta:
        crsf = False


class ChangePasswordForm(FlaskForm):
    password = PasswordField("New password", [InputRequired(), EqualTo('confirm', message=msg_password_match), DataRequired(message="Only using spaces not allowed")])
    confirm = PasswordField("Repeat new password")

    class Meta:
        crsf = False
