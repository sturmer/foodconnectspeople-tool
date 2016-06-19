from flask import Blueprint, render_template, request
from forms import SearchForm

from app import db
from app.search_recipe.forms import SearchForm
from app.search_recipe.models import Recipe

mod = Blueprint('search_recipe', __name__, url_prefix='/search_recipe')

@mod.route('/')
def home():
    return render_template('search_recipe/index.html')

@mod.route('/search/', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)
    if request.method == "GET":
        return render_template('search_recipe/search.html', form=form)
    elif request.method == "POST":
        print "Detected post method"
        return search_results(request.form)

    return render_template('search_recipe/search.html', form=form)

#@mod.route('/search_results/')
def search_results(form):
    keywords = form.get('keywords', '')
    gluten_free = form.get('gluten_free', False)
    lactose_free = form.get('lactose_free', False)
    vegetarian = form.get('vegetarian', False)
    vegan = form.get('vegan', False)
    data = {
            'keywords' : keywords,
            'gluten_free' : gluten_free,
            'lactose_free' : lactose_free,
            'vegan' : vegan,
            'vegetarian' : vegetarian
            }

    return render_template('search_recipe/search_results.html', data=data)
