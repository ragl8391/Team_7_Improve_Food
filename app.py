import os
from flask import Flask, render_template, redirect, url_for, request, jsonify, session
from pymongo import MongoClient
from dotenv import load_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix

load_dotenv()
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-change-me")  # to track user session

client = MongoClient(os.getenv("MONGO_URI"))
db = client["improve_food"]


@app.route("/")
def index():
    return render_template("landing.html")


@app.route("/marketplace")
def marketplace():
    # Placeholder: real query wire up
    food_items = []
    return render_template("marketplace.html", food_items=food_items)


# ---------- CART LOGIC ----------

def get_cart():
    """Cart is stored in session as: { item_id: quantity }"""
    return session.get("cart", {})


def save_cart(cart):
    session["cart"] = cart
    session.modified = True


@app.route("/cart/add/<item_id>", methods=["POST"])
def add_to_cart(item_id):
    cart = get_cart()
    cart[item_id] = cart.get(item_id, 0) + 1
    save_cart(cart)
    return jsonify({"success": True, "cart_count": sum(cart.values())})


@app.route("/cart/remove/<item_id>", methods=["POST"])
def remove_from_cart(item_id):
    cart = get_cart()
    cart.pop(item_id, None)
    save_cart(cart)
    return jsonify({"success": True, "cart_count": sum(cart.values())})


@app.route("/cart/update/<item_id>", methods=["POST"])
def update_cart_quantity(item_id):
    quantity = int(request.form.get("quantity", 1))
    cart = get_cart()
    if quantity <= 0:
        cart.pop(item_id, None)
    else:
        cart[item_id] = quantity
    save_cart(cart)
    return jsonify({"success": True, "cart_count": sum(cart.values())})


@app.route("/cart")
def view_cart():
    cart = get_cart()
    # Placeholder: real query + total calculation
    items = []
    order_total = 0
    return render_template("cart.html", items=items, order_total=order_total)


# ---------- CHECKOUT ----------

@app.route("/checkout")
def checkout():
    cart = get_cart()
    if not cart:
        return redirect(url_for("marketplace"))
    # Placeholder: real query + total calculation
    items = []
    order_total = 0
    return render_template("checkout.html", items=items, order_total=order_total)


@app.route("/checkout/confirm", methods=["POST"])
def confirm_claim():
    fulfillment_type = request.form.get("fulfillment_type")
    address = request.form.get("address")
    selected_time = request.form.get("time_window")
    cart = get_cart()
    # Placeholder: save the order to MongoDB here, using cart contents
    save_cart({})  # clear cart after order is placed
    return f"Order placed: {fulfillment_type}, time: {selected_time}"


@app.route("/check-radius", methods=["POST"])
def check_radius():
    data = request.get_json()
    return jsonify({"allowed": True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)