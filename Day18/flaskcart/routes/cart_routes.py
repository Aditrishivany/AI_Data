from flask import Blueprint, request, jsonify
from models.cart_model import *
from utils.helpers import response
from datetime import datetime

cart_bp = Blueprint("cart", __name__)

@cart_bp.route("/cart/add", methods=["POST"])
def add():
    data = request.json
    data["added_at"] = datetime.utcnow()
    add_to_cart(data)
    return jsonify(response(True, "Added to cart"))

@cart_bp.route("/cart/<user_id>", methods=["GET"])
def get(user_id):
    return jsonify(response(True, "Cart fetched", get_cart(user_id)))

@cart_bp.route("/cart/update/<id>", methods=["PUT"])
def update(id):
    update_quantity(id, request.json["quantity"])
    return jsonify(response(True, "Quantity updated"))

@cart_bp.route("/cart/remove/<id>", methods=["DELETE"])
def remove(id):
    remove_cart_item(id)
    return jsonify(response(True, "Item removed"))