from pymongo import MongoClient, errors
from pydantic import BaseModel


class MongoDB:
    client = None
    db = None

    def __init__(self):
        try:
            # try to instantiate a client instance
            # self.client = client = MongoClient('mongodb://barkeeper:barkeeper@127.0.0.1/cocktailmachine')
            self.client = client = MongoClient("mongodb://mongodb:27017")
            self.db = client.cocktailmachine

            # print the version of MongoDB server if connection successful
            print("server version:", client.server_info()["version"])
        except errors.ServerSelectionTimeoutError as err:
            # set the client instance to 'None' if exception
            self.client = None

            # catch pymongo.errors.ServerSelectionTimeoutError
            print("pymongo ERROR:", err)

    def get_db(self):
        return self.db


class Ingredient(BaseModel):
    name: str
    dispenser = -1


class Recipe(BaseModel):
    name: str
    ingredients: list
