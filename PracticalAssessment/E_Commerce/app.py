# =====================================================
# IMPORTS
# =====================================================
import os
import uuid
from functools import wraps

from flask import (
    Flask, render_template, request,
    redirect, url_for, abort,
    session, jsonify
)
from flask_login import (
    login_user, logout_user,
    login_required, current_user
)
from werkzeug.utils import secure_filename

from extensions import db, login_manager
from models import User, Product


# =====================================================
# APPLICATION CONFIGURATION
# =====================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret123"
app.config["SQLALCHEMY_DATABASE_URI"] =  \
    "sqlite:///" + os.path.join(BASE_DIR, "app.db")
app.config["UPLOAD_FOLDER"] = os.path.join(BASE_DIR, "static", "uploads")

db.init_app(app)
login_manager.init_app(app)


# =====================================================
# TOKEN-BASED AUTH (FOR API)
# =====================================================
api_tokens = {}  # In-memory token storage


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token or token not in api_tokens.values():
            return jsonify({"message": "Unauthorized"}), 401

        return f(*args, **kwargs)

    return decorated


# =====================================================
# LOGIN MANAGER (FOR WEB AUTH)
# =====================================================
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# =====================================================
# ===================== API ROUTES ====================
# =====================================================

# -------- API LOGIN --------
@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()

    user = User.query.filter_by(
        username=data.get("username"),
        password=data.get("password")
    ).first()

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    token = str(uuid.uuid4())
    api_tokens[user.username] = token

    return jsonify({
        "message": "Login successful",
        "token": token
    })


# -------- GET ALL PRODUCTS --------
@app.route("/api/products", methods=["GET"])
def get_products():
    products = Product.query.all()

    result = []
    for p in products:

        # Handle both local files and external URLs
        if p.image and p.image.startswith("http"):
            image_url = p.image
        elif p.image:
            image_url = url_for('static', filename='uploads/' + p.image, _external=True)
        else:
            image_url = None

        result.append({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "description": p.description,
            "image_url": image_url
        })

    return jsonify(result)


# -------- GET SINGLE PRODUCT --------
@app.route("/api/products/<int:id>", methods=["GET"])
def get_product(id):
    product = Product.query.get(id)

    if not product:
        return jsonify({"message": "Product not found"}), 404

    if product.image and product.image.startswith("http"):
        image_url = product.image
    elif product.image:
        image_url = url_for('static', filename='uploads/' + product.image, _external=True)
    else:
        image_url = None

    return jsonify({
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "image_url": image_url
    })



# -------- CREATE PRODUCT --------
@app.route("/api/products", methods=["POST"])
@token_required
def create_product():

    data = request.get_json()

    if not data.get("image_url"):
        return jsonify({"message": "Image URL required"}), 400

    product = Product(
        name=data.get("name"),
        price=data.get("price"),
        description=data.get("description"),
        image=data.get("image_url")  # store URL directly
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product created with image URL"}), 201


# -------- UPDATE PRODUCT --------
@app.route("/api/products/<int:id>", methods=["PUT"])
@token_required
def update_product(id):
    product = Product.query.get(id)

    if not product:
        return jsonify({"message": "Product not found"}), 404

    data = request.get_json()

    product.name = data.get("name", product.name)
    product.price = data.get("price", product.price)
    product.description = data.get("description", product.description)

    db.session.commit()

    return jsonify({"message": "Product updated"})


# -------- DELETE PRODUCT --------
@app.route("/api/products/<int:id>", methods=["DELETE"])
@token_required
def delete_product_api(id):
    product = Product.query.get(id)

    if not product:
        return jsonify({"message": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted"})


# =====================================================
# ===================== WEB ROUTES ====================
# =====================================================

# -------- HOME / PRODUCTS PAGE --------
@app.route("/")
@login_required
def products():
    products = Product.query.all()
    print("PRODUCTS:", products)
    return render_template("products.html", products=products)

# -------- REGISTER --------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            password=request.form["password"]
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("register.html")


# -------- LOGIN --------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(
            username=request.form["username"],
            password=request.form["password"]
        ).first()

        if user:
            login_user(user)
            return redirect(url_for("products"))

    return render_template("login.html")


# -------- LOGOUT --------
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


# -------- PRODUCT DETAIL --------
@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = Product.query.get(product_id)

    if not product:
        return abort(404)

    related = Product.query.filter(
        Product.id != product.id,
        Product.price.between(product.price - 500,
                              product.price + 500)
    ).limit(3).all()

    return render_template(
        "product_detail.html",
        product=product,
        related=related
    )


# ===================== PAYMENT =======================

@app.route("/payment", methods=["GET", "POST"])
@login_required
def payment():
    cart_ids = session.get("cart", [])
    products = Product.query.filter(
        Product.id.in_(cart_ids)
    ).all()

    if not products:
        return redirect(url_for("products"))

    total = sum([p.price for p in products])

    if request.method == "POST":
        # Simulate successful payment
        session["cart"] = []  # Clear cart after payment
        return render_template(
            "payment_success.html",
            total=total
        )

    return render_template(
        "payment.html",
        products=products,
        total=total
    )

# =====================================================
# ===================== CART SYSTEM ===================
# =====================================================

@app.route("/add-to-cart/<int:product_id>")
@login_required
def add_to_cart(product_id):
    product = Product.query.get(product_id)
    if not product:
        return abort(404)

    cart = session.get("cart", [])
    cart.append(product_id)
    session["cart"] = cart

    return redirect(url_for("products"))


@app.route("/cart")
@login_required
def cart():
    cart_ids = session.get("cart", [])
    products = Product.query.filter(
        Product.id.in_(cart_ids)
    ).all()

    total = sum([p.price for p in products])

    return render_template(
        "cart.html",
        products=products,
        total=total
    )


@app.route("/checkout")
@login_required
def checkout():
    cart_ids = session.get("cart", [])
    products = Product.query.filter(
        Product.id.in_(cart_ids)
    ).all()

    total = sum([p.price for p in products])

    return render_template(
        "checkout.html",
        products=products,
        total=total
    )


# =====================================================
# ===================== ADMIN ROUTES ==================
# =====================================================

@app.route("/add-product", methods=["GET", "POST"])
@login_required
def add_product():
    if not current_user.is_admin:
        return "Unauthorized", 403

    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        description = request.form["description"]
        image = request.files["image"]

        filename = secure_filename(image.filename)
        image.save(
            os.path.join(app.config["UPLOAD_FOLDER"], filename)
        )

        product = Product(
            name=name,
            price=price,
            description=description,
            image=filename
        )

        db.session.add(product)
        db.session.commit()

        return redirect(url_for("products"))

    return render_template("add_products.html")


@app.route("/delete-product/<int:product_id>")
@login_required
def delete_product(product_id):
    if not current_user.is_admin:
        return "Unauthorized", 403

    product = Product.query.get(product_id)
    if not product:
        return abort(404)

    db.session.delete(product)
    db.session.commit()

    return redirect(url_for("products"))


# =====================================================
# ===================== MAIN ENTRY ====================
# =====================================================

if __name__ == "__main__":
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    with app.app_context():
        db.create_all()

        # Create default admin
        if not User.query.filter_by(username="admin").first():
            admin = User(
                username="admin",
                password="admin",
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()

    #print(app.url_map)
    app.run(host="0.0.0.0", port=5000, debug=True)
    
