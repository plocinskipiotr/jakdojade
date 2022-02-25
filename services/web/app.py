import datetime
import sys
from pathlib import Path

from flask import Flask, jsonify

ROOT_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(ROOT_DIR))
print(sys.path)
from backend.src.endpoints_queries import get_cities, get_routes, get_stops

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify(time=datetime.datetime.now())


@app.route('/public_transport/cities')
def cities():
    cities = get_cities()
    return cities


@app.route('/public_transport/city/<string:city>/routes')
def city_routes(city):
    routes = get_routes(city)
    return routes


@app.route('/public_transport/city/<string:city>/closest_stops')
def closest_stop(city: str, latitude: float, longitude: float):
    stops = get_stops(city, longitude, latitude)
    return stops
