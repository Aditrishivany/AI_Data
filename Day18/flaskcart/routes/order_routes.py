from flask import Blueprint, request, jsonify
from models.order_model import *
from utils.helpers import response
from datetime import datetime

order_bp = Blueprint("orders", __name__)

@order_bp.route("/order", methods=["POST"])
def place():
    data = request.json
    data["created_at"] = datetime.utcnow()
    place_order(data)
    return jsonify(response(True, "Order placed"))

@order_bp.route("/orders/<user_id>", methods=["GET"])
def get_orders_route(user_id):
    return jsonify(response(True, "Orders fetched", get_orders(user_id)))

@order_bp.route("/order/<id>", methods=["GET"])
def get_order_route(id):
    return jsonify(response(True, "Order fetched", get_order(id)))