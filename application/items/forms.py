from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, validators
from wtforms.validators import ValidationError, InputRequired, EqualTo, Length, DataRequired
from application.categories.models import Category
from application.utils.errormessages import msg_name_length

class ItemForm(FlaskForm):
    name = StringField("Name", [InputRequired(), Length(min=1,max=144, message=msg_name_length), DataRequired(message="Only using spaces not allowed")])
    bought = BooleanField("Bought")
    amount = IntegerField("Amount", [validators.optional()])
    category = IntegerField("Category", [InputRequired()])

    class Meta:
        csrf = False

class ItemEditForm(FlaskForm):
    name = StringField("Name", [InputRequired(), Length(min=1,max=144, message=msg_name_length), DataRequired(message="Only using spaces not allowed")])
    bought = BooleanField("Bought")
    amount = IntegerField("Amount", [validators.optional()])
    category = IntegerField("Category", [InputRequired()])
    list = IntegerField("List", [InputRequired()])

    class Meta:
        csrf = False
