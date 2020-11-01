from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from models import Recipe, MongoDB, Ingredient
# from gpio import Dispenser
import json
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


mongo = MongoDB()

app = FastAPI()


# Index Route
@app.get("/")
async def root():
    return {"data": "Welcome to the cocktailmachine!"}


# Recipe routes
# get all recipes
@app.get('/apiv1/recipe', status_code=200)
async def get_all_recipes():
    recipes = []
    for recipe in mongo.get_db().recipe.find():
        recipes.append(Recipe(**recipe))
    return {'data': recipes}


# get recipe by name
@app.get('/apiv1/recipe/{name}', status_code=200)
async def get_recipe_by_name(name: str):
    req = mongo.get_db().recipe.find_one({"name": name})
    if req is None:
        raise HTTPException(status_code=404, detail="Error: Recipe not found")

    recipe = Recipe(**req)
    return {'data': recipe}


# delete recipe by name
@app.delete('/apiv1/recipe/{name}', status_code=200)
async def delete_recipe(name: str):
    req = mongo.get_db().recipe.find_one({"name": name})
    if req is None:
        raise HTTPException(status_code=404, detail="Error: Recipe not found")
    else:
        mongo.get_db().recipe.remove({"name": name})
        recipe = Recipe(**req)
        return {"data": recipe}


# update recipe by name Todo: Test and optimize
@app.put('/apiv1/recipe/{name}', status_code=200)
async def update_recipe_name(name: str, recipe: Recipe):
    # Check if name exists
    req = mongo.get_db().recipe.find_one({"name": name})
    if req is None:
        raise HTTPException(status_code=404, detail="Error: Recipe not found")

    # Todo: Check if new name doesn't exist
    nameExists = False

    if nameExists is True:
        raise HTTPException(status_code=200, detail="Error: Recipe with same name already exists")

    mongo.get_db().recipe.update({"name": name}, {"$set": {"name": recipe.name}})
    return {'data': recipe}


def get_ingredient_ids(name):
    recipe = Recipe(**mongo.get_db().recipe.find_one({"name": name}))
    ingredientsIds = []
    # add all ingredient ids in a list
    for ingredient in recipe.ingredients:
        print(ingredient)
        ingredientsIds.append(ingredient['ingredientId'])
    return ingredientsIds


def get_ingredients(name):
    recipe = Recipe(**mongo.get_db().recipe.find_one({"name": name}))
    ingredients = []
    # add all ingredient ids in a list
    for ingredient in recipe.ingredients:
        ingredients.append(ingredient)
    return ingredients


# check by name if cocktail is mixable
@app.get('/apiv1/recipe/{name}/mixable', status_code=200)
async def is_cocktail_mixable(name: str):
    recipeExists = False
    # get all recipes and check if a recipe with this name exists
    recipes = []
    for recipe in mongo.get_db().recipe.find():
        recipes.append(Recipe(**recipe))
    for recipe in recipes:
        if recipe.name == name:
            recipeExists = True

    if recipeExists is False:
        raise HTTPException(status_code=404, detail='Error: This Recipe does not exist')

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
    return {'data': mixable}


@app.get('/apiv1/recipe/{name}/mix')
async def mix_cocktail(name: str):
    # !!!UNCOMMENT FOR RASPBERRY PI!!!
    # activate dispensers
    # dispenser0 = Dispenser(18)
    # dispenser1 = Dispenser(23)
    # dispenser2 = Dispenser(24)
    # dispenser3 = Dispenser(25)

    dispenser_return_message = []

    for ingredient in get_ingredients(name):
        ingredient_id = ingredient['ingredientId']
        ingredients_amount = ingredient['amount']
        for dispenser in mongo.get_db().ingredient.find({"_id": ObjectId(ingredient_id)}):
            dispenser_number = dispenser['dispenser']
            if dispenser_number == 0:
                # dispenser0.on(ingredients_amount)
                disp0 = "Dispenser " + str(dispenser_number) + " triggered for " + str(ingredients_amount) + "cl."
                dispenser_return_message.append(disp0)
            elif dispenser_number == 1:
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

    return {'message': dispenser_return_message}


# create a new recipe
@app.post('/apiv1/recipe', status_code=201)
async def create_recipe(new_recipe: Recipe):
    # get all recipes and check if a recipe with the same name exists already
    recipes = []
    for recipe in mongo.get_db().recipe.find():
        recipes.append(Recipe(**recipe))
    for recipe in recipes:
        if recipe.name == new_recipe.name:
            raise HTTPException(status_code=200, detail='Error: Recipe with same name already exists')

    # if not, then save new recipe
    # Todo: Check if the IDs of the ingredients exist!
    json_compatible_data = jsonable_encoder(new_recipe)
    mongo.get_db().recipe.insert(json_compatible_data)
    return {'data': new_recipe}


# Ingredient Routes
# get all ingredients
@app.get('/apiv1/ingredient', status_code=200)
async def get_all_ingredients():
    ingredients = []
    for ingredient in mongo.get_db().ingredient.find():
        ingredients.append(Ingredient(**ingredient))
    return {"data": ingredients}


# get one ingredient by name
@app.get('/apiv1/ingredient/{name}', status_code=200)
async def get_ingredient_by_name(name: str):
    req = mongo.get_db().ingredient.find_one({"name": name})
    if req is None:
        raise HTTPException(status_code=404, detail='Error: No Ingredient with this name found')

    ingredient = Ingredient(**req)
    result = {
        'id': str(req['_id']),
        'name': ingredient.name,
        'dispenser': ingredient.dispenser
    }
    # print(result)
    return {'data': result}


# create a new ingredient
@app.post('/apiv1/ingredient', status_code=201)
async def create_ingredient(new_ingredient: Ingredient):
    # get all ingredients and check if a ingredient with same name exists
    ingredients = []
    for ingredient in mongo.get_db().ingredient.find():
        ingredients.append(Ingredient(**ingredient))
    for ingredient in ingredients:
        if ingredient.name == new_ingredient.name:
            raise HTTPException(status_code=200, detail='Error: Ingredient with same name already exists')

    # if not, then save new ingredient
    json_compatible_data = jsonable_encoder(new_ingredient)
    mongo.get_db().ingredient.insert(json_compatible_data)
    return {'data': new_ingredient}


# update ingredient by name
@app.put('/apiv1/ingredient/{name}', status_code=201)
async def update_ingredient_by_name(name: str, updateIngredient: Ingredient):
    # Check if name exists
    req = mongo.get_db().ingredient.find_one({"name": name})
    if req is None:
        raise HTTPException(status_code=404, detail='Error: No Ingredient with this name found')

    mongo.get_db().ingredient.update(
        {"name": name},
        {"$set": jsonable_encoder(updateIngredient)}
    )

    return {'data': updateIngredient}


# Reset Route - Only for Postman testing purposes
@app.get('/apiv1/reset')
async def reset_data():
    mongo.get_db().recipe.remove()
    mongo.get_db().ingredient.remove()
    return {"data": "All Data deleted"}
