import datetime
import sys
from pathlib import Path

from flask import Flask, jsonify

ROOT_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(ROOT_DIR))
print(sys.path)
from backend.src.endpoints_queries import get_cities, get_routes

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
