import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)



@app.route('/')
def Home(): 
    return "Hello World"





if __name__ == '__main__':
    app.run(debug=True)
