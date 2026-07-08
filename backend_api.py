import math
from flask import Flask, request, jsonify

app = Flask(__name__)


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

@app.route('/')
def home():
    return "The Backend API is running successfully!"

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
    return jsonify(item_data), 201

@app.route('/reserve-item', methods=['POST'])
def reserve_item():
    item_id = request.form.get('item_id')
    
    # 1. Extract location data from the incoming request form
    user_lat = request.form.get('user_lat')
    user_lon = request.form.get('user_lon')
    restaurant_lat = request.form.get('restaurant_lat')
    restaurant_lon = request.form.get('restaurant_lon')
    
    # 2. Bundle into tuples (converting incoming strings to floats)
    # 2.5 Validate all coordinate boundaries first
    if (not (-90 <= float(user_lat) <= 90) or 
        not (-180 <= float(user_lon) <= 180) or 
        not (-90 <= float(restaurant_lat) <= 90) or 
        not (-180 <= float(restaurant_lon) <= 180)):
        
        return jsonify(error="Invalid coordinates. Latitude must be between -90/90 and longitude between -180/180."), 400

    user_coord = (float(user_lat), float(user_lon))
    restaurant_coord = (float(restaurant_lat), float(restaurant_lon))

    delivery_available = True # PLACEHOLDER TODO: PROVIDE CORRECT VALUE FROM MONGODB
    
    # 3. Calculate the distance using the helper function
    distance = calculate_distance(restaurant_coord, user_coord)
    
    # 4. Enforce delivery rules
    if distance <= 5 and delivery_available:
        # TODO: MONGODB RESERVATION QUERIES HERE
        return jsonify(message="Item reserved successfully!"), 200
    elif distance > 5:
        return jsonify(error="Cannot deliver when distance is greater than 5 miles"), 400
    else:
        return jsonify(error="This restaurant does not offer delivery."), 400

if __name__ == '__main__':
    app.run(debug=True)

