from flask import Flask, render_template, jsonify
import psycopg2


app = Flask(__name__)

db_config = {
    "dbname": "db name",
    "user": "username",
    "password": "pasword",
    "host": "localhost",
    "port": "port"

}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_markers')
def get_markers():

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT ")