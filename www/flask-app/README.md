# Start application

1. Make sure to source flask-virtual/bin/activate

2. Create DB

```
python shell.py
>>> from app import db
>>> db.create_all()
>>> exit()
```

3. Run:

`python run.py`


# Recipes

## Query DB from cli

```
python shell.py
>>> from app.recipes.models import Recipe
>>> Recipe.query.all()
```
