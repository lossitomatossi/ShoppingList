from flask_wtf import FlaskForm
from wtforms import StringField

class ItemForm(FlaskForm):
    name = StringField("Item name")

    class Meta:
        csrf = False
