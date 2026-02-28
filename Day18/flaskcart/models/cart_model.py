from utils.db import db
from bson import ObjectId

cart = db.cart

def add_to_cart(data):
    return cart.insert_one(data)

def get_cart(user_id):
    return list(cart.find({"user_id": user_id}))

def update_quantity(cart_id, qty):
    return cart.update_one({"_id": ObjectId(cart_id)}, {"$set": {"quantity": qty}})

def remove_cart_item(cart_id):
    return cart.delete_one({"_id": ObjectId(cart_id)})