from pymongo import MongoClient
from main import settings

client = MongoClient(settings.mongo_client)
db = client[settings.db_name]
collection = db[settings.collection_name]


