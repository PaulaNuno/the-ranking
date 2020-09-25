import os
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient

PORT = os.getenv("PORT")
DBURL = os.getenv("DB_URL")

client = MongoClient(DBURL)
db = client.get_database()
