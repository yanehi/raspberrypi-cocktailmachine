import pymongo

# database connection
# client = pymongo.MongoClient("mongodb://barkeeper:barkeeper@127.0.0.1/cocktailmachine")
client = pymongo.MongoClient("mongodb://mongodb:27017/")

# create database cocktailmachine
db = client["cocktailmachine"]

recipe_collection = db["recipe"]
recipe_list = [
    {
        "name": "Vodka Shot",
        "ingredients": [
            {
                "ingredientId": "5f9760bc3c54e107bf5fd64d",
                "amount": 4
            }
        ]
    },
    {
        "name": "Vodka-O",
        "ingredients": [
            {
                "ingredientId": "5f9760bc3c54e107bf5fd64d",
                "amount": 4
            },
            {
                "ingredientId": "5f9760bc3c54e107bf5fd653",
                "amount": 10
            }
        ]
    },
    {
        "name": "Cuba Libre",
        "ingredients": [
            {
                "ingredientId": "5f9760bc3c54e107bf5fd64b",
                "amount": 4
            },
            {
                "ingredientId": "5f9760bc3c54e107bf5fd64c",
                "amount": 10
            }
        ]
    },
    {
        "name": "Copa-mixable",
        "ingredients": [
            {
                "ingredientId": "5f9760bc3c54e107bf5fd64c",
                "amount": 3
            },
            {
                "ingredientId": "5f9760bc3c54e107bf5fd64c",
                "amount": 2
            },
            {
                "ingredientId": "5f9760bc3c54e107bf5fd64b",
                "amount": 1
            },
            {
                "ingredientId": "5f9760bc3c54e107bf5fd64d",
                "amount": 3
            }
        ]
    },
    {
        "name": "Copa-No-mixable",
        "ingredients": [
            {
                "ingredientId": "5f9760bc3c54e107bf5fd659",
                "amount": 9
            },
            {
                "ingredientId": "5f9760bc3c54e107bf5fd658",
                "amount": 8
            }
        ]
    },
    {
        "name": "Copa-No-mixable2",
        "ingredients": [
            {
                "ingredientId": "5f9760bc3c54e107bf5fd657",
                "amount": 1
            },
            {
                "ingredientId": "5f9760bc3c54e107bf5fd656",
                "amount": 3
            }
        ]
    },
    {
        "name": "Wasser",
        "ingredients": [
            {
                "ingredientId": "5f9760bc3c54e107bf5fd651",
                "amount": 10
            }
        ]
    },
    {
        "name": "Mischbar",
        "ingredients": [
            {
                "ingredientId": "5f9760bc3c54e107bf5fd64d",
                "amount": 3
            }
        ]
    }
]

# insert values in ingredients collection
recipe_collection.insert_many(recipe_list)
