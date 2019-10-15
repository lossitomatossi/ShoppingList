from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import ValidationError, InputRequired, EqualTo, Length
from application.utils.errormessages import msg_name_length


class CategoryForm(FlaskForm):
    name = StringField("Category name", [InputRequired(), Length(min=1,max=144, message=msg_name_length)])

    class Meta:
        csrf = False
