import math
import os
import certifi

from flask import Flask, request, jsonify
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
        return "The Backend API and MongoDB are running successfully!"
    except Exception as error:
        print("MongoDB error:", error)
        return f"MongoDB connection failed: {error}", 500
    
@app.route('/add-item', methods=['POST'])
def add_item():
    item_name = request.form.get('item_name')
    quantity = request.form.get('quantity')
    expiry = request.form.get('expiry')
    item_data = {
        "name": item_name,
        "quantity": quantity,
        "expiry": expiry,
        "status": "available", 
        "message": "Item added successfully!"
    }

    result = food_items_collection.insert_one(item_data)

    item_data["_id"] = str(result.inserted_id)

    return jsonify(item_data), 201

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
    if (not (-90 <= float(user_lat) <= 90) or 
        not (-180 <= float(user_lon) <= 180) or 
        not (-90 <= float(restaurant_lat) <= 90) or 
        not (-180 <= float(restaurant_lon) <= 180)):
        
        return jsonify(error="Invalid coordinates. Latitude must be between -90/90 and longitude between -180/180."), 400

    user_coord = (float(user_lat), float(user_lon))
    restaurant_coord = (float(restaurant_lat), float(restaurant_lon))

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
