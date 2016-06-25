from app import db
from app.recipes import constants as RECIPE

class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(RECIPE.NAME_LENGTH), index=True, nullable=False, unique=True)
    procedure = db.Column(db.String(RECIPE.PROCEDURE_MAX_LENGTH), nullable=False)
    preparation_time_minutes = db.Column(db.SmallInteger)
    difficulty = db.Column(db.SmallInteger)
    place_of_origin = db.String(1024)
    category = db.Column(db.String(1024))
    cooking_technique = db.Column(db.String(1024))
    is_vegetarian = db.Column(db.Boolean)
    is_vegan = db.Column(db.Boolean)
    is_gluten_free = db.Column(db.Boolean)
    is_lactose_free = db.Column(db.Boolean)

    def __init__(self):
        # TODO
        pass

    def __repr__(self):
        return '<Recipe %s>' % (self.name)
    
