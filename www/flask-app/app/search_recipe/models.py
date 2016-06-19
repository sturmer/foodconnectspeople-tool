from app import db
#from app.search_recipe import constants

class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    thumbnail = db.Column(db.Binary)
    name = db.Column(db.String(1024), index=True, nullable=False)
    preparation_time_minutes = db.Column(db.SmallInteger)
    difficulty = db.Column(db.SmallInteger)
    place_of_origin = db.String(1024)
    is_from_latitude = db.Column(db.Numeric(9,6))
    is_from_longitude = db.Column(db.Numeric(9,6))
    category = db.Column(db.String(1024))
    cooking_technique = db.Column(db.String(1024))
    is_vegetarian = db.Column(db.Boolean)
    is_vegan = db.Column(db.Boolean)
    is_gluten_free = db.Column(db.Boolean)
    is_lactose_free = db.Column(db.Boolean)

    def __repr__(self):
        return '<Recipe %s>' % (self.name)
