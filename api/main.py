from bson import ObjectId
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


# delete recipe by name
@app.delete('/apiv1/recipe/{name}')
async def delete_recipe(name: str):
    if mongo.get_db().recipe.remove({"name": name}):
        return True
    else:
        return False


# mix cocktail
@app.get('/apiv1/recipe/{name}/mix')
async def is_cocktail_mixable(name: str):
    # check if cocktail is mixable
    mixable = False

    # check if all dispenser ids are not -1
    recipes = []
    for recipe in mongo.get_db().recipe.find({"name": name}):
        recipes.append(Recipe(**recipe))

    ingredient_ids = []

    # add all ingredient ids in a list
    for counter in range(len(recipe['ingredients'])):
        ingredient_ids.append(recipe['ingredients'][counter]['ingredientId'])

    # check for every ingredient by its id if dispenser is not -1
    for ingredient_id in ingredient_ids:
        # if one dispenser value of an ingredient is -1 set mixable false and break the loop
        if mongo.get_db().ingredient.find({"$and": [{"_id": ObjectId(ingredient_id)}, {"dispenser": -1}]}).count() > 0:
            mixable = False
            break
        else:
            mixable = True
    return mixable


# not working now...
@app.post('/apiv1/recipe/{name}')
async def create_recipe(recipe: Recipe):
    for ingredient in range(len(recipe.ingredients)):
        mongo.get_db().recipe.insert({
            "name": recipe.name,
            "ingredients": [
                {
                    "ingredientId": recipe.ingredients[ingredient]['ingredientId'],
                    "amount": recipe.ingredients[ingredient]['amount']
                }
            ]})
