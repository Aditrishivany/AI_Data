# app.py
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/churn_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/patterns")
def patterns():
    return render_template("patterns.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = [float(x) for x in request.form.values()]
    arr = np.array(data).reshape(1,-1)
    pred = model.predict(arr)[0]
    return render_template("index.html", result=pred)

if __name__ == "__main__":
    app.run(debug=True)