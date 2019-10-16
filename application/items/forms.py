from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, validators
from wtforms.validators import ValidationError, InputRequired, EqualTo, Length
from application.categories.models import Category
from application.utils.errormessages import msg_name_length

class ItemForm(FlaskForm):
    name = StringField("Name", [InputRequired(), Length(min=1,max=144, message=msg_name_length)])
    bought = BooleanField("Bought", [InputRequired()])
    amount = IntegerField("Amount", [InputRequired()])
    category = IntegerField("Category", [InputRequired()])

    class Meta:
        csrf = False
