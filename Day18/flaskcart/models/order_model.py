from utils.db import db
from bson import ObjectId

orders = db.orders

def place_order(data):
    return orders.insert_one(data)

def get_orders(user_id):
    return list(orders.find({"user_id": user_id}))

def get_order(order_id):
    return orders.find_one({"_id": ObjectId(order_id)})