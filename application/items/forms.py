from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, validators

class ItemForm(FlaskForm):
    name = StringField("Item name", [validators.Length(min=2)])
    bought = BooleanField("Done")
    amount = IntegerField("Amount")

    class Meta:
        csrf = False
