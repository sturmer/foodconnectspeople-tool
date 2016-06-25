from flask import Blueprint, render_template, request
from forms import SearchForm

from app import db
#from app.recipes import constants as RECIPE
from app.recipes.forms import SearchForm, CreationForm
from app.recipes.models import Recipe

mod = Blueprint('recipes', __name__, url_prefix='/recipes')

@mod.route('/')
def index():
    return render_template('recipes/index.html')

@mod.route('/search/', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)
    if request.method == "GET":
        return render_template('recipes/search.html', form=form)
    elif request.method == "POST":
        print "Detected post method"

        # TODO Actually use the information provided to do a query IN THIS FUNCTION! (at least, in this route)
        #keywords = request.form.get('keywords', '')
        #gluten_free = request.form.get('gluten_free', False)
        #lactose_free = request.form.get('lactose_free', False)
        #vegetarian = request.form.get('vegetarian', False)
        #vegan = request.form.get('vegan', False)
        #data = {
        #        'keywords' : keywords,
        #        'gluten_free' : gluten_free,
        #        'lactose_free' : lactose_free,
        #        'vegan' : vegan,
        #        'vegetarian' : vegetarian
        #        }

        return render_template('recipes/recipe_list.html', recipes=None)

    return render_template('recipes/search.html', form=form)

@mod.route('/recipe_list/')
def recipe_list(recipes):
    return render_template('recipes/recipe_list.html', recipes=recipes)

@mod.route('/list/')
def list():
    recipes = Recipe.query.all()
    return render_template('recipes/recipe_list.html', recipes=recipes)

@mod.route('/insert/', methods=['GET', 'POST'])
def insert():
    '''
    Show a form to insert a recipe
    '''

    form = CreationForm(request.form)

    if request.method == 'POST':
        recipe = Recipe()

        recipe.name = request.form.get('name')
        recipe.procedure = request.form.get('procedure')
        recipe.preparation_time_minutes =  request.form.get('preparation_time_minutes', 60)
        recipe.difficulty =  request.form.get('difficulty', 3)
        recipe.place_of_origin =  request.form.get('place_of_origin', '')
        recipe.category = request.form.get('category', 'Cooked')
        recipe.cooking_technique = request.form.get('cooking_technique', '')

        for intolerance in ['is_vegetarian', 'is_vegan', 'is_gluten_free', 'is_lactose_free']:
            if request.form.get(intolerance) == 'y':
                setattr(recipe, intolerance, True)
            else:
                setattr(recipe, intolerance, False)

        #recipe.is_vegan = request.form.get('is_vegan', False)
        #recipe.is_gluten_free = request.form.get('is_gluten_free', False)
        #recipe.is_lactose_free = request.form.get('is_lactose_free', False)

        # Save to DB
        db.session.add(recipe)
        db.session.commit()

        return render_template('recipes/recipe.html', recipe=recipe)
    else:
        return render_template('recipes/insert.html', form=form)

@mod.route('/recipe/<recipe_id>')
def show_recipe(recipe_id):
    result_set = Recipe.query.filter_by(id=recipe_id)
    hits = result_set.count()
    if hits == 1:
        recipe = result_set.one()
        return render_template('recipes/recipe.html', recipe=recipe)
    elif hits == 0:
        return render_template('recipes/recipe_list.html', recipe=Recipe.query.all())
    else:
        # Error: more results with the same ID??
        pass
