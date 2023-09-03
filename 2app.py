from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Marker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    neighborhood = db.Column(db.String(255))
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)
    room_type = db.Column(db.String(255))
    price = db.Column(db.Float)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/vacation_safety_db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/markers')
def markers():

    markers = Marker.query.all()
    markers_data = [{'neighbourhood': marker.neighbourhood, 'latitude': marker.latitude, 'longitude': marker.longitude, 'room_type': marker.room_type, 'price': marker.price} for marker in markers]
    print(markers_data)
    
    return jsonify(markers_data)

if __name__ == '__main__':
    app.run(debug=True)