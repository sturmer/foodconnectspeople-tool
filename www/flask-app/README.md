# Start application

1. Make sure to source flask-virtual/bin/activate

2. Create DB (creates app.db)

```
python shell.py
>>> from app import db
>>> db.create_all()
>>> exit()
```

3. Run:

`python run.py`


# Recipes (for some activity, not for cooking!)

## Query DB from cli

```
python shell.py
>>> from app.recipes.models import Recipe
>>> Recipe.query.all()
```
## Drop all tables

There's a more sophisticated example at: https://bitbucket.org/zzzeek/sqlalchemy/wiki/UsageRecipes/DropEverything
But more simply:

```
python shell.py
>>> from app import db
>>> db.drop_all()
```
