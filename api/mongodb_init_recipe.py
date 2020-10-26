import pymongo

# database connection
client = pymongo.MongoClient("mongodb://barkeeper:barkeeper@127.0.0.1/cocktailmachine")

# create database cocktailmachine
db = client["cocktailmachine"]

recipe_collection = db["recipe"]
recipe_list = [
    {
        "name": "Vodka Shot",
        "ingredients": [
            {
                "ingredientId": "5f947e94945e70d35915df9b",
                "amount": 4
            }
        ]
    },
    {
        "name": "Vodka-O",
        "ingredients": [
            {
                "ingredientId": "5f947e94945e70d35915df9b",
                "amount": 4
            },
            {
                "ingredientId": "5f947e94945e70d35915dfa1",
                "amount": 30
            }
        ]
    },
    {
        "name": "Cuba Libre",
        "ingredients": [
            {
                "ingredientId": "5f947e94945e70d35915df99",
                "amount": 4
            },
            {
                "ingredientId": "5f947e94945e70d35915df9a",
                "amount": 30
            }
        ]
    },
    {
        "name": "Copa-mixable",
        "ingredients": [
            {
                "ingredientId": "5f947e94945e70d35915df9d",
                "amount": 9
            },
            {
                "ingredientId": "5f947e94945e70d35915df9a",
                "amount": 99
            },
            {
                "ingredientId": "5f947e94945e70d35915df9b",
                "amount": 10
            },
            {
                "ingredientId": "5f947e94945e70d35915df9c",
                "amount": 32
            }
        ]
    },
    {
        "name": "Copa-No-mixable",
        "ingredients": [
            {
                "ingredientId": "5f947e94945e70d35915df9d",
                "amount": 9
            },
            {
                "ingredientId": "5f947e94945e70d35915df9a",
                "amount": 8
            }
        ]
    },
    {
        "name": "Copa-No-mixable2",
        "ingredients": [
            {
                "ingredientId": "5f947e94945e70d35915df9c",
                "amount": 1
            },
            {
                "ingredientId": "5f947e94945e70d35915dfa0",
                "amount": 12
            }
        ]
    },
    {
        "name": "Copa-No-mixable3",
        "ingredients": [
            {
                "ingredientId": "5f947e94945e70d35915dfa2",
                "amount": 8
            },
            {
                "ingredientId": "5f947e94945e70d35915dfa2",
                "amount": 45
            }
        ]
    },
    {
        "name": "Wasser",
        "ingredients": [
            {
                "ingredientId": "5f947e94945e70d35915df9f",
                "amount": 300
            }
        ]
    },
    {
        "name": "Mischbar",
        "ingredients": [
            {
                "ingredientId": "5f947e94945e70d35915df9a",
                "amount": 300
            }
        ]
    }
]

# insert values in ingredients collection
recipe_collection.insert_many(recipe_list)
