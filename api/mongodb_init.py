import pymongo

# database connection
client = pymongo.MongoClient("mongodb://mongodb:27017/")

# create database cocktailmachine
db = client["cocktailmachine"]

# create collection ingredient in database cocktailmachine
ingredient_collection = db["ingredient"]

# values for collection ingredients
ingredients_list = [
    {"name": "Rum", "dispenser": 1},
    {"name": "Cola", "dispenser": 2},
    {"name": "Vodka", "dispenser": 3},
    {"name": "Fanta", "dispenser": 4},
    {"name": "Jack Daniels", "dispenser": -1},
    {"name": "Havanna", "dispenser": -1},
    {"name": "Sodawasser", "dispenser": -1},
    {"name": "Energy", "dispenser": -1},
    {"name": "Osaft", "dispenser": -1},
    {"name": "Berliner Luft", "dispenser": -1},
    {"name": "Doppelkorn", "dispenser": -1},
    {"name": "Gin", "dispenser": -1},
    {"name": "Tomatensaft", "dispenser": -1},
    {"name": "Zuckersirup", "dispenser": -1},
    {"name": "Limettensaft", "dispenser": -1}
]

recipe_collection = db["recipe"]
recipe_list = [
    {
        "name": "Vodka Shot",
        "ingredients": [
            {
                "ingredientId": "5f937ebe332aac8e12626cce",
                "amount": 4
            }
        ]
    },
    {
        "name": "Vodka-O",
        "ingredients": [
            {
                "ingredientId": "5f937ebe332aac8e12626cce",
                "amount": 4
            },
            {
                "ingredientId": "5f937ebe332aac8e12626cd4",
                "amount": 30
            }
        ]
    },
    {
        "name": "Cuba Libre",
        "ingredients": [
            {
                "ingredientId": "5f937ebe332aac8e12626ccc",
                "amount": 4
            },
            {
                "ingredientId": "5f937ebe332aac8e12626ccd",
                "amount": 30
            }
        ]
    }
]

# insert values in ingredients collection
ingredient_collection.insert_many(ingredients_list)
recipe_collection.insert_many(recipe_list)
