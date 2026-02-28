from flask import Blueprint, request, jsonify
from models.product_model import *
from utils.helpers import response
from datetime import datetime

product_bp = Blueprint("products", __name__)

@product_bp.route("/products", methods=["POST"])
def create():
    data = request.json
    data["created_at"] = datetime.utcnow()
    add_product(data)
    return jsonify(response(True, "Product added"))

@product_bp.route("/products", methods=["GET"])
def get_all():
    return jsonify(response(True, "Products fetched", get_all_products()))

@product_bp.route("/products/<id>", methods=["GET"])
def get_one(id):
    prod = get_product(id)
    return jsonify(response(True, "Product fetched", prod))

@product_bp.route("/products/<id>", methods=["PUT"])
def update(id):
    update_product(id, request.json)
    return jsonify(response(True, "Product updated"))

@product_bp.route("/products/<id>", methods=["DELETE"])
def delete(id):
    delete_product(id)
    return jsonify(response(True, "Product deleted"))