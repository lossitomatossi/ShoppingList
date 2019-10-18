from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.validators import ValidationError, InputRequired, EqualTo, Length, DataRequired
from application.utils.errormessages import msg_name_length


class CategoryForm(FlaskForm):
    name = StringField("Category name", [InputRequired(), Length(min=1,max=144, message=msg_name_length), DataRequired(message="Only using spaces not allowed")])

    class Meta:
        csrf = False
