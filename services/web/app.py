import datetime
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(ROOT_DIR))

from flask import Flask, jsonify, request
from backend.src.endpoints_queries import get_cities, get_routes, get_stops
from backend.src.user import User
from backend.src.db_init import db_init


db_init()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return jsonify(time=datetime.datetime.now())


@app.route('/public_transport/cities', methods=['GET'])
def cities():
    cities = get_cities()
    return cities


@app.route('/public_transport/city/<string:city>/routes', methods=['GET'])
def city_routes(city):
    routes = get_routes(city)
    return routes


@app.route('/public_transport/city/<string:city>/stop', methods=['GET'])
def closest_stop(city: str):
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    age = int(request.args.get('age', 25))
    stops = get_stops(city, User(latitude, longitude, age))
    return stops
