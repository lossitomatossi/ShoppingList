from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, validators
from wtforms.validators import ValidationError, InputRequired, EqualTo, Length
from application.categories.models import Category

class ItemForm(FlaskForm):
    name = StringField("Name", [InputRequired(), Length(min=1,max=144)])
    bought = BooleanField("Bought", [InputRequired()])
    amount = IntegerField("Amount", [InputRequired()])

    class Meta:
        csrf = False


class ItemCreateForm(FlaskForm):
    name = StringField("Name", [InputRequired(), Length(min=2)])
    bought = BooleanField("Bought", [InputRequired()])
    amount = IntegerField("Amount", [InputRequired()])
    category = IntegerField("Category", [InputRequired()])

    class Meta:
        crsf = False
