from fastapi import FastAPI
from models import Recipe, MongoDB

mongo = MongoDB()

app = FastAPI()


# Index Route
@app.get("/")
async def root():
    return {"message": "Welcome to the cocktailmachine!"}


# Recipe routes
# get all recipes
@app.get('/apiv1/recipe')
async def get_all_recipes():
    recipes = []
    for recipe in mongo.get_db().recipe.find():
        recipes.append(Recipe(**recipe))
    return {'recipes': recipes}


# get recipe by name
@app.get('/apiv1/recipe/{name}')
async def get_recipe_by_name(name: str):
    recipes = []
    for recipe in mongo.get_db().recipe.find({"name": name}):
        recipes.append(Recipe(**recipe))
    return {'recipes': recipes}


# get recipe by name
@app.delete('/apiv1/recipe/{name}')
async def delete_recipe(name: str):
    if mongo.get_db().recipe.remove({"name": name}):
        return True
    else:
        return False
