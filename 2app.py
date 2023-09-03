from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

db = SQLAlchemy()

class Airbnb(db.Model):
    __tablename__ = 'airbnbs'
    id = db.Column(db.Integer, primary_key=True)
    neighbourhood = db.Column(db.String(255))
    latitude = db.Column(db.Numeric)
    longitude = db.Column(db.Numeric)
    room_type = db.Column(db.String(255))
    price = db.Column(db.Numeric)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mypostgres:postgres@localhost:5432/vacation_safety_db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/airbnb')
def airbnb_data():

    try:
        airbnb_data = Airbnb.query.all()

        results = [{'neighbourhood': data.neighbourhood, 'latitude': data.latitude, 'longitude': data.longitude, 'room_type': data.room_type, 'price': data.price} for data in airbnb_data]
        print(results)
    
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)