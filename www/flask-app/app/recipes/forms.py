from flask_wtf import Form
from wtforms import StringField, BooleanField, FileField, IntegerField,\
    SelectField
from wtforms.validators import InputRequired, Length, NumberRange

class SearchForm(Form):
    keywords        = StringField('Keywords')
    gluten_free     = BooleanField("Gluten-free")
    lactose_free    = BooleanField("Lactose-free")
    vegetarian      = BooleanField("Vegetarian")
    vegan           = BooleanField("Vegan")

class CreationForm(Form):
    thumbnail = FileField('Image') #, [FileAllowed(['jpg', 'png'], 'Images only!')]
    name = StringField('Name', [InputRequired()])
    preparation_time_minutes = IntegerField('Preparation time (minutes)', [Length(min=0)])
    difficulty = IntegerField('Difficulty', [NumberRange(min=0, max=10)])
    place_of_origin = StringField('Origin')
    category = StringField('Category')
    cooking_technique = SelectField('Cooking technique', choices=[('raw', 'Raw'), ('cooked', 'Cooked')])
    is_vegetarian = BooleanField("Is vegetarian?")
    is_vegan = BooleanField("Is vegan?")
    is_gluten_free = BooleanField("Is gluten-free?")
    is_lactose_free = BooleanField("Is lactose-free?")
