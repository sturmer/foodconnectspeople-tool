from wtforms import Form, StringField, BooleanField #, validators

class SearchForm(Form):
    keywords = StringField('Keywords')
    gluten_free = BooleanField("Gluten-free")
    lactose_free = BooleanField("Lactose-free")
    vegetarian = BooleanField("Vegetarian")
    vegan = BooleanField("Vegan")


