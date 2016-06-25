from flask_wtf import Form
from wtforms import StringField, BooleanField, FileField, IntegerField,\
    SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, NumberRange

class SearchForm(Form):
    keywords        = StringField('Keywords')
    gluten_free     = BooleanField("Gluten-free")
    lactose_free    = BooleanField("Lactose-free")
    vegetarian      = BooleanField("Vegetarian")
    vegan           = BooleanField("Vegan")

class CreationForm(Form):
    # The photo(s) don't go to the DB, but get stored in the static/img folder
    thumbnail = FileField('Image') #, [FileAllowed(['jpg', 'png'], 'Images only!')]

    name = StringField('Name', [InputRequired()])
    procedure = TextAreaField('Procedure', [InputRequired()])
    preparation_time_minutes = IntegerField('Preparation time (minutes)', [Length(min=0)])
    difficulty = SelectField('Difficulty', choices=[
        (1, u"\u2605"),
        (2, u"\u2605\u2605"),
        (3, u"\u2605\u2605\u2605"),
        (4, u"\u2605\u2605\u2605\u2605"),
        (5, u"\u2605\u2605\u2605\u2605\u2605")
        ])
    place_of_origin = StringField('Origin')     # XXX Should this be a list of countries in DB?
    category = StringField('Category')  # TODO Must become a SelectField
    cooking_technique = SelectField('Cooking technique', choices=[('raw', 'Raw'), ('cooked', 'Cooked')])
    is_vegetarian = BooleanField("Is vegetarian?")
    is_vegan = BooleanField("Is vegan?")
    is_gluten_free = BooleanField("Is gluten-free?")
    is_lactose_free = BooleanField("Is lactose-free?")
