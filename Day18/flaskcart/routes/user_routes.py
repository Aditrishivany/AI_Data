from flask import Blueprint, request, jsonify
from models.user_model import create_user, find_user_by_email
from utils.helpers import hash_password, verify_password, response
from datetime import datetime
from bson import ObjectId
from utils.db import db

user_bp = Blueprint("user", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    required = ["name", "email", "password", "phone", "address"]

    for field in required:
        if field not in data:
            return jsonify(response(False, f"{field} is required")), 400

    if find_user_by_email(data["email"]):
        return jsonify(response(False, "Email already exists")), 400

    data["password"] = hash_password(data["password"])
    data["created_at"] = datetime.utcnow()

    create_user(data)
    return jsonify(response(True, "User registered successfully"))

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = find_user_by_email(data["email"])

    if not user:
        return jsonify(response(False, "Invalid email or password")), 401

    if not verify_password(data["password"], user["password"]):
        return jsonify(response(False, "Invalid email or password")), 401

    return jsonify(response(True, "Login successful", {"user_id": str(user["_id"])}))

@user_bp.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    user = db.users.find_one({"_id": ObjectId(user_id)})

    if not user:
        return jsonify({"error": "User not found"}), 404

    user["_id"] = str(user["_id"])
    return jsonify(user)