import math
import os
import certifi

from flask import Flask, request, jsonify, render_template
from bson import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient

app = Flask(__name__)

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri, tlsCAFile=certifi.where(), serverSelectionTimeoutMS=5000)

db = client["improve_food"]
food_items_collection = db["food_items"]

# --- Helper Function ---
def calculate_distance(restaurant_coord, user_coord):
    R = 3956.0  # Radius of the Earth in miles
    
    # 1. Unpack the tuples
    lat1, lon1 = restaurant_coord
    lat2, lon2 = user_coord
    
    # 2. Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # 3. Calculate differences
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # 4. Haversine formula math
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Calculate the final distance
    distance = R * c
    
    return distance

@app.route("/")
def home():
    try:
        client.admin.command("ping")
        return render_template("landing.html")
    except Exception as error:
        print("MongoDB error:", error)
        return f"MongoDB connection failed: {error}", 500

@app.route("/marketplace")
def marketplace():
    try:
        food_items = list(
            food_items_collection.find({"status": "available"})
        )

        return render_template(
            "marketplace.html",
            food_items=food_items
        )

    except Exception as error:
        print("Marketplace MongoDB error:", error)
        return f"Marketplace failed: {error}", 500
@app.route("/add-food")
def add_food():
    return render_template("add_food.html")

@app.route("/restaurant-location")
def restaurant_location():
    return render_template("restaurant_location.html")

@app.route("/cart")
def view_cart():
    return render_template("cart.html")

@app.route("/checkout")
def checkout():
    items = []
    order_total = 0.00

    return render_template(
        "checkout.html",
        items=items,
        order_total=order_total
    )


@app.route("/confirm-claim", methods=["POST"])
def confirm_claim():
    fulfillment_type = request.form.get("fulfillment_type")
    time_window = request.form.get("time_window")
    address = request.form.get("address")

    return render_template(
        "confirmation.html",
        order_total=0.00,
        fulfillment_type=fulfillment_type,
        time_window=time_window,
        address=address
    )


@app.route("/check-radius", methods=["POST"])
def check_radius():
    data = request.get_json(silent=True) or {}

    item_id = data.get("item_id")
    user_lat = data.get("user_lat")
    user_lon = data.get("user_lon")

    if not item_id:
        return jsonify(
            allowed=False,
            error="No item was selected."
        ), 400

    try:
        mongo_item_id = ObjectId(item_id)
        user_lat = float(user_lat)
        user_lon = float(user_lon)
    except (TypeError, ValueError):
        return jsonify(
            allowed=False,
            error="Invalid item ID or coordinates."
        ), 400

    if not (-90 <= user_lat <= 90):
        return jsonify(
            allowed=False,
            error="Latitude must be between -90 and 90."
        ), 400

    if not (-180 <= user_lon <= 180):
        return jsonify(
            allowed=False,
            error="Longitude must be between -180 and 180."
        ), 400

    item = food_items_collection.find_one({
        "_id": mongo_item_id
    })

    if item is None:
        return jsonify(
            allowed=False,
            error="Item not found."
        ), 404

    restaurant_location = item.get("restaurant_location", {})
    restaurant_lat = restaurant_location.get("lat")
    restaurant_lon = restaurant_location.get("lon")

    if restaurant_lat is None or restaurant_lon is None:
        return jsonify(
            allowed=False,
            error="Restaurant location is unavailable."
        ), 400

    try:
        restaurant_lat = float(restaurant_lat)
        restaurant_lon = float(restaurant_lon)
    except (TypeError, ValueError):
        return jsonify(
            allowed=False,
            error="Restaurant coordinates are invalid."
        ), 400

    distance = calculate_distance(
        (restaurant_lat, restaurant_lon),
        (user_lat, user_lon)
    )

    delivery_available = item.get(
        "delivery_available",
        False
    )

    allowed = delivery_available and distance <= 5

    return jsonify(
        allowed=allowed,
        distance_miles=round(distance, 2)
    ), 200


@app.route("/confirmation")
def confirmation():
    return render_template(
        "confirmation.html",
        order_total=0.00
    )

# Returns one specific food item identified by its MongoDB ID.  
@app.route("/api/items/<item_id>", methods=["GET"])
def retrieve_item(item_id):
    try:
        mongo_item_id = ObjectId(item_id)
    except Exception:
        return jsonify(error="Invalid item ID."), 400

    item = food_items_collection.find_one({
        "_id": mongo_item_id
    })

    if item is None:
        return jsonify(error="Item not found."), 404

    return jsonify({
        "_id": str(item["_id"]),
        "name": item.get("name"),
        "restaurant_name": item.get("restaurant_name"),
        "quantity": item.get("quantity"),
        "expires_at": item.get("expires_at") or item.get("expiry"),
        "status": item.get("status"),
        "delivery_available": item.get(
            "delivery_available",
            True
        )
    }), 200


# Returns all currently available food items from the MongoDB food_items collection.
@app.route("/api/items", methods=["GET"])
def retrieve_items():
    try:
        items = food_items_collection.find({"status": "available"})

        results = []

        for item in items:
            results.append({
                "_id": str(item["_id"]),
                "name": item.get("name"),
                "restaurant_name": item.get("restaurant_name"),
                "quantity": item.get("quantity"),
                "expires_at": item.get("expires_at") or item.get("expiry"),
                "status": item.get("status"),
                "delivery_available": item.get(
                    "delivery_available",
                    True
                )
            })

        return jsonify(results), 200

    except Exception as error:
        return jsonify(error=str(error)), 500

@app.route("/add-item", methods=["POST"])
def add_item():
    item_name = request.form.get("item_name")
    restaurant_name = request.form.get("restaurant_name")
    email = request.form.get("email")
    category = request.form.get("category")
    description = request.form.get("food_description")
    price = request.form.get("price")
    quantity = request.form.get("quantity")
    expires_at = (
        request.form.get("expires_at")
        or request.form.get("expiry")
    )

    if not item_name or not restaurant_name or not quantity or not expires_at:
        return jsonify(
            error=(
                "item_name, restaurant_name, quantity, "
                "and expires_at are required."
            )
        ), 400

    item_data = {
        "name": item_name,
        "restaurant_name": restaurant_name,
        "email": email,
        "category": category,
        "description": description,
        "quantity": quantity,
        "price": price,
        "expires_at": expires_at,
        "status": "available",
        "delivery_available": True
    }

    result = food_items_collection.insert_one(item_data)

    return jsonify({
        "_id": str(result.inserted_id),
        **item_data,
        "message": "Item added successfully!"
    }), 201

@app.route('/reserve-item', methods=['POST'])
def reserve_item():
    item_id = request.form.get('item_id')
    
    try:
        mongo_item_id = ObjectId(item_id)
    except Exception:
        return jsonify(error="Invalid item ID."), 400

    item = food_items_collection.find_one({"_id": mongo_item_id})

    if item is None:
        return jsonify(error="Item not found."), 404

    if item.get("status") != "available":
        return jsonify(error="This item has already been reserved."), 409

    # 1. Extract location data from the incoming request form
    
    user_lat = request.form.get('user_lat')
    user_lon = request.form.get('user_lon')
    restaurant_lat = request.form.get('restaurant_lat')
    restaurant_lon = request.form.get('restaurant_lon')
    
    try:
        user_lat = float(user_lat)
        user_lon = float(user_lon)
        restaurant_lat = float(restaurant_lat)
        restaurant_lon = float(restaurant_lon)
    except (TypeError, ValueError):
        return jsonify(
            error="All coordinates must be valid numbers."), 400
    
    # 2. Bundle into tuples (converting incoming strings to floats)
    # 2.5 Validate all coordinate boundaries first
    if (not (-90 <= user_lat <= 90) or 
        not (-180 <= user_lon <= 180) or 
        not (-90 <= restaurant_lat <= 90) or 
        not (-180 <= restaurant_lon <= 180)):
        
        return jsonify(error="Invalid coordinates. Latitude must be between -90/90 and longitude between -180/180."), 400

    user_coord = (user_lat, user_lon)
    restaurant_coord = (restaurant_lat, restaurant_lon)

    delivery_available = item.get("delivery_available", True)

    distance = calculate_distance(
        restaurant_coord,
        user_coord
    )
    
    # 3. Calculate the distance using the helper function
    # 4. Enforce delivery rules
    if distance <= 5 and delivery_available:
        update_result = food_items_collection.update_one(
            {
                "_id": mongo_item_id,
                "status": "available"
            },
            {
                "$set": {
                    "status": "reserved"
                }
            }
        )

        if update_result.modified_count == 0:
            return jsonify(
                error="Another user already reserved this item."
            ), 409

        return jsonify(
            message="Item reserved successfully!"
        ), 200

    elif distance > 5:
        return jsonify(
            error="Cannot deliver when distance is greater than 5 miles"
        ), 400

    else:
        return jsonify(
            error="This restaurant does not offer delivery."
        ), 400
    

if __name__ == "__main__":
    app.run(debug=True)
