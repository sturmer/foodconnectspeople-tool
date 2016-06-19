from flask import Flask, render_template, request, redirect
from forms import SearchForm

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if request.method == "GET":
        return render_template('search.html', form=form)
    elif request.method == "POST":
        return search_results(request.form)

    return render_template('search.html', form=form)

@app.route('/search_results')
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
    return render_template('search_results.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

