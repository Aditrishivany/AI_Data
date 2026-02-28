import os
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# ----------------------------
# IMAGE UPLOAD CONFIG
# ----------------------------
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return "About page"

@app.route("/namm")
def homes():
    return render_template("index.html", name="Aditri")

@app.route("/login", methods=["GET", "POST"])
def login():
    return "Login"

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/form")
def fo():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]
    return f"Welcome {username}"


# ----------------------------
# NEW IMAGE UPLOAD ROUTES
# ----------------------------
@app.route("/upload")
def upload_page():
    return render_template("image.html")

@app.route("/upload_image", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return "No file part"

    file = request.files["image"]

    if file.filename == "":
        return "No image selected"
    
    if file and allowed_file(file.filename):
        # Save file in /static/uploads/
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        return render_template("image.html", uploaded_image=filepath)

    return "Invalid file type"


if __name__ == "__main__":
    app.run(debug=True)
