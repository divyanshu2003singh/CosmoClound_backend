from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

client = MongoClient("Write the connection url here")
db = client["ecommerce"]
products_collection = db["products"]
orders_collection = db["orders"]
