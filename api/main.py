from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from models import Recipe, MongoDB, Ingredient
import json
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


# from api.gpio import Dispenser

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


# update recipe name
@app.put('/apiv1/recipe/{name}')
async def update_recipe_name(name: str, recipe: Recipe):
    mongo.get_db().recipe.update({"name": name}, {"$set": {"name": recipe.name}})
    return {'recipe': recipe}


def get_ingredient_ids(name):
    recipes = []
    for recipe in mongo.get_db().recipe.find({"name": name}):
        recipes.append(Recipe(**recipe))

    ingredient_ids = []

    # add all ingredient ids in a list
    for counter in range(len(recipe['ingredients'])):
        ingredient_ids.append(recipe['ingredients'][counter]['ingredientId'])
    return ingredient_ids


def get_ingredients(name):
    recipes = []
    for recipe in mongo.get_db().recipe.find({"name": name}):
        recipes.append(Recipe(**recipe))

    ingredients = []

    # add all ingredient ids in a list
    for counter in range(len(recipe['ingredients'])):
        ingredients.append(recipe['ingredients'][counter])
    return ingredients


# check by name if cocktail is mixable
@app.get('/apiv1/recipe/{name}/mixable')
async def is_cocktail_mixable(name: str):
    # check if cocktail is mixable
    mixable = False

    ingredient_ids = get_ingredient_ids(name)

    # check for every ingredient by its id if dispenser is not -1
    for ingredient_id in ingredient_ids:
        # if one dispenser value of an ingredient is -1 set mixable false and break the loop
        if mongo.get_db().ingredient.find({"$and": [{"_id": ObjectId(ingredient_id)}, {"dispenser": -1}]}).count() > 0:
            mixable = False
            break
        else:
            mixable = True
    return mixable


@app.get('/apiv1/recipe/{name}/mix')
async def mix_cocktail(name: str):
    # !!!UNCOMMENT FOR RASPBERRY PI!!!
    # activate dispensers
    # dispenser1 = Dispenser(18)
    # dispenser2 = Dispenser(23)
    # dispenser3 = Dispenser(24)
    # dispenser4 = Dispenser(25)

    dispenser_return_message = []

    for ingredient in get_ingredients(name):
        ingredient_id = ingredient['ingredientId']
        ingredients_amount = ingredient['amount']
        for dispenser in mongo.get_db().ingredient.find({"_id": ObjectId(ingredient_id)}, {"dispenser": 1}):
            dispenser_number = dispenser['dispenser']
            if dispenser_number == 1:
                # dispenser1.on(ingredients_amount)
                disp1 = "Dispenser " + str(dispenser_number) + " triggered for " + str(ingredients_amount) + "cl."
                dispenser_return_message.append(disp1)
            elif dispenser_number == 2:
                # dispenser2.on(ingredients_amount)
                disp2 = "Dispenser " + str(dispenser_number) + " triggered for " + str(ingredients_amount) + "cl."
                dispenser_return_message.append(disp2)
            elif dispenser_number == 3:
                # dispenser3.on(ingredients_amount)
                disp3 = "Dispenser " + str(dispenser_number) + " triggered for " + str(ingredients_amount) + "cl."
                dispenser_return_message.append(disp3)
            elif dispenser_number == 4:
                # dispenser4.on(ingredients_amount)
                disp4 = "Dispenser " + str(dispenser_number) + " triggered for " + str(ingredients_amount) + "cl."
                dispenser_return_message.append(disp4)

    return {'message': dispenser_return_message}


# not working now...
@app.post('/apiv1/recipe/')
async def create_recipe(recipe: Recipe):
    json_compatible_data = jsonable_encoder(recipe)
    mongo.get_db().recipe.insert(json_compatible_data)
    return {'created': recipe}


### Ingredient Routes

# get all ingredients
@app.get('/apiv1/ingredient')
async def get_all_ingredients():
    ingredients = []
    for ingredient in mongo.get_db().ingredient.find():
        ingredients.append(Ingredient(**ingredient))
    return {"ingredients": ingredients}


# get one ingredient by name
@app.get('/apiv1/ingredient/{name}')
async def get_ingredient_by_name(name: str):
    req = mongo.get_db().ingredient.find_one({"name": name})
    if req == None:
        return {'error': 'No Ingredient with this name found'}

    ingredient = Ingredient(**req)
    result = {
        'id': str(req['_id']),
        'name': ingredient.name,
        'dispenser': ingredient.dispenser
    }
    print(result)
    return {'ingredient': result}


# create a new ingredient
@app.post('/apiv1/ingredient')
async def create_ingredient(newIngredient: Ingredient):
    # get all ingredients and check if a ingredient with same name exists
    ingredients = []
    for ingredient in mongo.get_db().ingredient.find():
        ingredients.append(Ingredient(**ingredient))
    for ingredient in ingredients:
        if ingredient.name == newIngredient.name:
            return {'error': 'Ingredient with same name already exists'}

    # if not, then save new ingredient
    json_compatible_data = jsonable_encoder(newIngredient)
    mongo.get_db().ingredient.insert_one(json_compatible_data)
    return {'ingredient': newIngredient}


# update ingredient by name
@app.put('/apiv1/ingredient/{name}')
async def update_ingredient_by_name(name: str, updateIngredient: Ingredient):
    req = mongo.get_db().ingredient.find_one_and_update(
        {"name": name},
        {"$set": jsonable_encoder(updateIngredient)}
    )
    if req == None:
        return {'error': 'No Ingredient with this name found'}
    return {'ingredient': updateIngredient}


# Reset Route - Only for Postman testing purposes
@app.get('/apiv1/reset')
async def reset_data():
    mongo.get_db().recipe.delete_many({})
    mongo.get_db().ingredient.delete_many({})
    return {"data": "deleted"}
