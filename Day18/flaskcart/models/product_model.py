from utils.db import db
from bson import ObjectId

products = db.products

def add_product(data):
    return products.insert_one(data)

def get_all_products():
    return list(products.find())

def get_product(id):
    return products.find_one({"_id": ObjectId(id)})

def update_product(id, data):
    return products.update_one({"_id": ObjectId(id)}, {"$set": data})

def delete_product(id):
    return products.delete_one({"_id": ObjectId(id)})