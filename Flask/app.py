from flask import Flask, jsonify, request
import json
import psycopg2
from configparser import ConfigParser
from config import config

app = Flask(__name__)

# Load configuration from JSON file
with open('config.json') as config_file:
    config_data = json.load(config_file)  # Use a different variable name

# Database connection configuration
db_config = {
    "dbname": config_data['database']['dbname'],  
    "user": config_data['database']['user'],     
    "password": config_data['database']['password'],  
    "host": config_data['database']['host'],          
    "port": config_data['database']['port']          
}

# Function to establish a database connection
def connect_db():
    conn = psycopg2.connect(**db_config)
    return conn

# API route to retrieve data from "airbnbs" table
@app.route("/api/airbnbs", methods=["GET"])
def get_airbnbs_data():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # SQL query for "airbnbs" table
        query = "SELECT id, neighborhood, latitude, longitude, room_type, price FROM airbnbs"
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Convert rows to a list of dictionaries
        data = []
        for row in rows:
            data.append({
                "id": row[0],
                "neighborhood": row[1],
                "latitude": float(row[2]),
                "longitude": float(row[3]),
                "room_type": row[4],
                "price": float(row[5]),
            })

        conn.close()
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)})

# API route to retrieve data from "crash_locations" table
@app.route("/api/crash_locations", methods=["GET"])
def get_crash_locations_data():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # SQL query for "crash_locations" table
        query = "SELECT number, collision_date, collision_time, day_of_week, longitude, latitude FROM crash_locations"
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Convert rows to a list of dictionaries
        data = []
        for row in rows:
            data.append({
                "number": row[0],
                "collision_date": str(row[1]),
                "collision_time": str(row[2]),
                "day_of_week": row[3],
                "longitude": float(row[4]),
                "latitude": float(row[5]),
            })

        conn.close()
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)})

# API route to retrieve data from "crime" table
@app.route("/api/crime", methods=["GET"])
def get_crime_data():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # SQL query for "crime" table
        query = "SELECT neighborhood, crime_index, motor_vehicle_theft, total_violent_crime, total_burglary, total_thefts FROM crime"
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Convert rows to a list of dictionaries
        data = []
        for row in rows:
            data.append({
                "neighborhood": row[0],
                "crime_index": int(row[1]),
                "motor_vehicle_theft": int(row[2]),
                "total_violent_crime": int(row[3]),
                "total_burglary": int(row[4]),
                "total_thefts": int(row[5]),
            })

        conn.close()
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)