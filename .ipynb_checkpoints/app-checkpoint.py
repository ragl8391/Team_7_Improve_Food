import os
from flask import Flask, render_template, redirect, url_for, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix


load_dotenv()

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1)
client = MongoClient(os.getenv("MONGO_URI"))
db = client["improve_food"]

@app.route("/")
def index():
    return render_template("landing.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Placeholder: actual auth with MongoDB 
        return redirect(url_for("marketplace"))
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Person 3/4 will wire up actual account creation in MongoDB here
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/marketplace")
def marketplace():
    # Placeholder: real query wire up 
    food_items = []
    return render_template("marketplace.html", food_items=food_items)

@app.route("/checkout/<item_id>")
def checkout(item_id):
    # Placeholder: real data connection
    item = {"_id": item_id, "name": "Sample item", "restaurant_name": "Sample Restaurant"}
    return render_template("checkout.html", item=item)

@app.route("/checkout/<item_id>/confirm", methods=["POST"])
def confirm_claim(item_id):
    fulfillment_type = request.form.get("fulfillment_type")
    address = request.form.get("address")
    # Placeholder: saving the claim here
    return f"Claimed {item_id} as {fulfillment_type}"

@app.route("/check-radius", methods=["POST"])
def check_radius():
    # Placeholder: real distance calculation
    data = request.get_json()
    return jsonify({"allowed": True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)