from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
import sqlite3
import datetime

app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)

DATABASE = "database.db"


# ----------------------------
# Database Connection
# ----------------------------
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# ----------------------------
# Create Table
# ----------------------------
def create_table():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


create_table()


# ----------------------------
# Register User
# ----------------------------
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = get_db_connection()

    try:
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"message": "Username already exists"}), 400
    finally:
        conn.close()


# ----------------------------
# Login User
# ----------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = get_db_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    ).fetchone()
    conn.close()

    if user:
        access_token = create_access_token(
            identity=username,
            expires_delta=datetime.timedelta(hours=1)
        )
        return jsonify(access_token=access_token)

    return jsonify({"message": "Invalid credentials"}), 401


# ----------------------------
# Protected Route
# ----------------------------
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user)


# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)