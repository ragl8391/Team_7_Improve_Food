import os
import math
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

# ---------- RESTAURANT PAGES ----------

@app.route("/restaurant/add-food", methods=["GET", "POST"])
def add_food():
    if request.method == "POST":
        # Database/API integration will go here.
        return redirect(url_for("restaurant_location"))

    return render_template("add_food.html")


@app.route("/restaurant/location", methods=["GET", "POST"])
def restaurant_location():
    if request.method == "POST":
        # Database/API integration will go here.
        return redirect(url_for("index"))

    return render_template("restaurant_location.html")


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


# ---------- CHECKOUT DELIVERY ----------


# max radius for restuarat delivery
DELIVERY_RADIUS_MILES = 5

def haversine_distance(lat1, lon1, lat2, lon2):
    """Returns distance in miles between two lat/lon points."""
    R = 3958.8  # Earth radius in miles
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lon2 - lon1)
 
    a = math.sin(d_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


@app.route("/check-radius", methods=["POST"])
def check_radius():
    data = request.get_json()
    item_id = data.get("item_id")
    user_lat = data.get("user_lat")
    user_lon = data.get("user_lon")
 
    if not all([item_id, user_lat is not None, user_lon is not None]):
        return jsonify({"error": "Missing required fields"}), 400
 
    # Placeholder: look up the item's restaurant, then the restaurant's coordinates
    # item = db.food_items.find_one({"_id": ObjectId(item_id)})
    # restaurant = db.restaurants.find_one({"_id": item["restaurant_id"]})
    # restaurant_lat = restaurant["latitude"]
    # restaurant_lon = restaurant["longitude"]
    restaurant_lat, restaurant_lon = 39.7392, -104.9903  # placeholder coords (Denver)
 
    distance = haversine_distance(user_lat, user_lon, restaurant_lat, restaurant_lon)
    allowed = distance <= DELIVERY_RADIUS_MILES
 
    return jsonify({"allowed": allowed, "distance_miles": round(distance, 2)})

# ---------- CHECKOUT CONFIRMATION ----------

@app.route("/checkout/confirm", methods=["POST"])
def confirm_claim():
    fulfillment_type = request.form.get("fulfillment_type")
    address = request.form.get("address")
    selected_time = request.form.get("time_window")
    cart = get_cart()

    if not cart:
        return redirect(url_for("marketplace"))

    # Placeholder: pull real item docs + restaurant info from MongoDB using cart contents
    # item_ids = [ObjectId(i) for i in cart.keys()]
    # items = list(db.food_items.find({"_id": {"$in": item_ids}}))
    # restaurant = db.restaurants.find_one({"_id": items[0]["restaurant_id"]})
    items = []
    order_total = 0
    restaurant_name = "Sample Restaurant"
    restaurant_location = "123 Main St, Denver, CO"

    # Placeholder: save the order to MongoDB here, using cart contents
    save_cart({})  # clear cart after order is placed

    return render_template(
        "confirmation.html",
        fulfillment_type=fulfillment_type,
        address=address,
        selected_time=selected_time,
        items=items,
        order_total=order_total,
        restaurant_name=restaurant_name,
        restaurant_location=restaurant_location,
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)