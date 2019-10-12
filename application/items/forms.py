from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, validators
from application.categories.models import Category

class ItemForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2)])
    bought = BooleanField("Bought")
    amount = IntegerField("Amount")

    class Meta:
        csrf = False


class ItemCreateForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2)])
    bought = BooleanField("Bought")
    amount = IntegerField("Amount")
    category = SelectField(u'Group', coerce=int)

    class Meta:
        crsf = False
