from pymongo.mongo_client import MongoClient
from app.environment.index import MONGO_URI


client = MongoClient(MONGO_URI)

print('Connected to MongoDB')

db = client.get_default_database()
