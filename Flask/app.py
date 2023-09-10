from flask import Flask, jsonify
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from connect import connect, config 
from sqlalchemy.types import TypeDecorator

app = Flask(__name__)

Base = declarative_base()

class Money(TypeDecorator):
    impl = String

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(String(10))
        else:
            return dialect.type_descriptor(String(10))

class Airbnb(Base):
    __tablename__ = 'airbnbs'

    id = Column(Integer, primary_key=True)
    neighborhood = Column(String(66))
    latitude = Column(Float)
    longitude = Column(Float)
    room_type = Column(String(66))
    price = Column(Money)

class CrashLocation(Base):
    __tablename__ = 'crash_locations'

    number = Column(Integer, primary_key=True)
    collision_date = Column(DateTime)
    collision_time = Column(String(8))
    day_of_week = Column(String(66))
    longitude = Column(Float)
    latitude = Column(Float)

class Crime(Base):
    __tablename__ = 'crime'

    neighborhood = Column(String(66), primary_key=True)
    crime_index = Column(Integer)
    motor_vehicle_theft = Column(Integer)
    total_violent_crime = Column(Integer)
    total_burglary = Column(Integer)
    total_thefts = Column(Integer)

# Database connection
connect()  

# Define your SQLAlchemy engine and session here
db_config = config()
db_uri = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)
session = Session()

# Define a route for the root URL
@app.route("/", methods=["GET"])
def home():
        #links to other endpoints
    airbnb_link = "<a href='/api/airbnbs'>Airbnb Data</a>"
    crash_locations_link = "<a href='/api/crash_locations'>Crash Locations</a>"
    crime_link = "<a href='/api/crime'>Crime Data</a>"

    # message with links
    message = f"Welcome to SD's Best Located Rentals!<br>{airbnb_link}<br>{crash_locations_link}<br>{crime_link}"

    return message
@app.route("/api/airbnbs", methods=["GET"])
def airbnbs():
    try:
        data = session.query(Airbnb).all()
        # Convert SQLAlchemy objects to dictionaries and jsonify
        result = [
            {
                "id": entry.id,
                "neighborhood": entry.neighborhood,
                "latitude": entry.latitude,
                "longitude": entry.longitude,
                "room_type": entry.room_type,
                "price": entry.price,
            }
            for entry in data
        ]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

# API route to retrieve data from "crash_locations" table
@app.route("/api/crash_locations", methods=["GET"])
def crash_locations():
    try:
        data = session.query(CrashLocation).all()
        result = [
            {
                "number": entry.number,
                "collision_date": str(entry.collision_date),
                "collision_time": str(entry.collision_time),
                "day_of_week": entry.day_of_week,
                "longitude": float(entry.longitude),
                "latitude": float(entry.latitude),
            }
            for entry in data
        ]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

# API route to retrieve data from "crime" table
@app.route("/api/crime", methods=["GET"])
def crime_data():
    try:
        data = session.query(Crime).all()
        result = [
            {
                "neighborhood": entry.neighborhood,
                "crime_index": int(entry.crime_index),
                "motor_vehicle_theft": int(entry.motor_vehicle_theft),
                "total_violent_crime": int(entry.total_violent_crime),
                "total_burglary": int(entry.total_burglary),
                "total_thefts": int(entry.total_thefts),
            }
            for entry in data
        ]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    # Get the database connection parameters from config.ini
    db_config = config()

    # Create SQLAlchemy engine
    db_uri = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
    engine = create_engine(db_uri)

    app.run(debug=True)
