from app import db
from app.recipes import constants as RECIPE

class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(RECIPE.NAME_LENGTH), index=True, nullable=False, unique=True)
    #procedure = db.Column(db.String(RECIPE.PROCEDURE_MAX_LENGTH), nullable=False)
    preparation_time_minutes = db.Column(db.SmallInteger)
    persons = db.Column(db.SmallInteger)
    difficulty = db.Column(db.SmallInteger)
    place_of_origin = db.String(1024)
    category = db.Column(db.String(1024))
    main_ingredient = db.Column(db.String(1024))
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

class RecipeIngredients(db.Model):
    __tablename__ = 'recipe_ingredients'
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), autoincrement=True, primary_key=True)
    ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    quantity = db.Column(db.SmallInteger)
    unit_of_measure = db.String(128)
    preparation_technique = db.Column(db.String(1024))
    alternative_ingredient = db.Column(db.String(1024))

    def __init__(self):
        # TODO
        pass

    def __repr__(self):
        return '<RecipeIngredients %d %d>' % (self.recipe_id, self.ingredient_id)
