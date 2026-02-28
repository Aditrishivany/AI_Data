from flask import Flask, render_template, request
from LoginTest.models import db, User

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Flask 3.x way
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter_by(username=username, password=password).first()

    if user:
        return "Login Successful", 200
    return "Invalid Credentials", 401
