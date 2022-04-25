import pymongo

client = pymongo.MongoClient("mongodb://localhost")

db = client["flask"]

users_collection = db["users"]
links_collection = db["links"]

