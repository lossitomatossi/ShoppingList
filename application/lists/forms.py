from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, validators
from wtforms.validators import ValidationError, InputRequired, EqualTo, Length
from application.utils.errormessages import msg_name_length, msg_info_length

class ListForm(FlaskForm):
    name = StringField("Name", [InputRequired(), Length(min=1,max=144, message=msg_name_length)])
    info = StringField("Info", [InputRequired(), Length(min=1,max=144, message=msg_info_length)])

    class Meta:
        csrf = False
