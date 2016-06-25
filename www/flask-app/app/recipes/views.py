from flask import Blueprint, render_template, request
from forms import SearchForm

from app import db
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

        return render_template('recipes/search_results.html', recipes=None)

    return render_template('recipes/search.html', form=form)

@mod.route('/search_results/')
def search_results(recipes):
    return render_template('recipes/search_results.html', recipes=recipes)

@mod.route('/list/')
def list():
    recipes = Recipe.query.all()
    return render_template('recipes/search_results.html', recipes=recipes)

@mod.route('/insert/', methods=['GET', 'POST'])
def insert():
    '''
    Show a form to insert a recipe
    '''

    form = CreationForm(request.form)

    if request.method == 'POST':
        recipe = Recipe()
        #recipe.id = ?
        recipe.name = request.form.get('name')
        # TODO And the other fields

        # Save to DB
        db.session.add(recipe)
        db.session.commit()

        return render_template('recipes/recipe.html', recipe=recipe)
    else:
        return render_template('recipes/insert.html', form=form)

@mod.route('/recipe/<recipe_id>')
def show_recipe(recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id)
    return render_template('recipes/recipe.html', recipe=recipe)
