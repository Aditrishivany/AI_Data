
from flask import Flask, render_template, request, redirect
import json
import os
from functools import wraps
from datetime import datetime

app = Flask(__name__)
DATA_FILE = "inventory.json"
LOG_FILE = "inventory.log"

# ============================
# DECORATOR (Logging)
# ============================

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now()} - {func.__name__} executed\n")
        return result
    return wrapper


# ============================
# BASE CLASS
# ============================

class Product:
    def __init__(self, pid, name, price, stock):
        self.__pid = pid
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_id(self):
        return self.__pid

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, qty):
        if self.__stock + qty < 0:
            raise ValueError("Stock cannot go below zero")
        self.__stock += qty

    def display(self):
        return f"{self.__pid} - {self.__name}"

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "pid": self.__pid,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }


# ============================
# SUBCLASSES
# ============================

class Electronics(Product):
    def __init__(self, pid, name, price, stock, warranty):
        super().__init__(pid, name, price, stock)
        self.__warranty = warranty

    def display(self):
        return super().display() + f" | Warranty: {self.__warranty} years"

    def to_dict(self):
        data = super().to_dict()
        data["warranty"] = self.__warranty
        return data


class Grocery(Product):
    def __init__(self, pid, name, price, stock, expiry):
        super().__init__(pid, name, price, stock)
        self.__expiry = expiry

    def display(self):
        return super().display() + f" | Expiry: {self.__expiry}"

    def to_dict(self):
        data = super().to_dict()
        data["expiry"] = self.__expiry
        return data


# ============================
# INVENTORY (Custom Iterator)
# ============================

class Inventory:
    def __init__(self):
        self.__products = []
        self.__index = 0
        self.load()

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__products):
            product = self.__products[self.__index]
            self.__index += 1
            return product
        raise StopIteration

    @log_action
    def add(self, product):
        self.__products.append(product)
        self.save()

    @log_action
    def remove(self, pid):
        self.__products = [p for p in self.__products if p.get_id() != pid]
        self.save()

    @log_action
    def update_stock(self, pid, qty):
        for p in self.__products:
            if p.get_id() == pid:
                p.update_stock(qty)
                self.save()
                return
        raise ValueError("Product not found")

    def search(self, keyword):
        return [p for p in self.__products if keyword.lower() in p.get_name().lower()]

    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump([p.to_dict() for p in self.__products], f, indent=4)

    def load(self):
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            for item in data:
                if item["type"] == "Electronics":
                    self.__products.append(Electronics(
                        item["pid"], item["name"],
                        item["price"], item["stock"],
                        item["warranty"]
                    ))
                elif item["type"] == "Grocery":
                    self.__products.append(Grocery(
                        item["pid"], item["name"],
                        item["price"], item["stock"],
                        item["expiry"]
                    ))


inventory = Inventory()


# ============================
# ROUTES
# ============================

@app.route("/")
def index():
    return render_template("index.html", products=list(inventory))

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        pid = request.form["pid"]
        name = request.form["name"]
        price = float(request.form["price"])
        stock = int(request.form["stock"])
        ptype = request.form["type"]
        extra = request.form["extra"]

        if ptype == "Electronics":
            product = Electronics(pid, name, price, stock, extra)
        else:
            product = Grocery(pid, name, price, stock, extra)

        inventory.add(product)
        return redirect("/")
    return render_template("add.html")

@app.route("/delete/<pid>")
def delete(pid):
    inventory.remove(pid)
    return redirect("/")

@app.route("/update/<pid>", methods=["POST"])
def update(pid):
    qty = int(request.form["qty"])
    inventory.update_stock(pid, qty)
    return redirect("/")

@app.route("/search", methods=["POST"])
def search():
    keyword = request.form["keyword"]
    results = inventory.search(keyword)
    return render_template("index.html", products=results)


if __name__ == "__main__":
    app.run(debug=True)
