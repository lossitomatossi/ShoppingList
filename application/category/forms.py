from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CategoryForm(FlaskForm):
    name = StringField("Item name", [validators.Length(min=1)])
    more_info = StringField("Category name")

    class Meta:
        csrf = False
