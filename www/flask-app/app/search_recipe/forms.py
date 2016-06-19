from flask_wtf import Form
from wtforms import StringField, BooleanField

class SearchForm(Form):
    keywords = StringField('Keywords')
    gluten_free = BooleanField("Gluten-free")
    lactose_free = BooleanField("Lactose-free")
    vegetarian = BooleanField("Vegetarian")
    vegan = BooleanField("Vegan")


