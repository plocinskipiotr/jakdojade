import datetime
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(ROOT_DIR))

from flask import Flask, jsonify, request
from backend.src.endpoints_queries import get_cities, get_routes, get_stops, get_trips
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
    routes = [item.serialize() for item in routes]
    routes = jsonify(routes)
    return routes


@app.route('/public_transport/city/<string:city>/stop', methods=['GET'])
def closest_stop(city: str):
    user_latitude = float(request.args.get('latitude'))
    user_longitude = float(request.args.get('longitude'))
    age = int(request.args.get('age', 25))
    stops = get_stops(city, User(user_latitude, user_longitude, age))
    stops = [item.serialize() for item in stops]
    stops = jsonify(stops)
    return stops

@app.route('/public_transport/city/<string:city>/departure', methods=['GET'])
def closest_departure(city: str):
    user_latitude = float(request.args.get('latitude'))
    user_longitude = float(request.args.get('longitude'))
    age = int(request.args.get('age', 25))
    stops = get_stops(city, User(user_latitude, user_longitude, age), stop_limit=1)
    res = get_trips(city,stops)
    #stops = [item.serialize() for item in stops]
    #stops = jsonify(stops)
    #return stops


# @app.route('/public_transport/city/<string:city>/departure', methods=['GET'])
# def closest_departure(city: str):
#     user_latitude = float(request.args.get('user_latitude'))
#     user_longitude = float(request.args.get('user_longitude'))
#     age = int(request.args.get('age', 25))
#     dest_latitude = float(request.args.get('dest_latitude'))
#     dest_longitude = float(request.args.get('dest_longitude'))
#
#     start_stop = get_stops(city, User(user_latitude, user_longitude, age), stop_limit=1)[0]
#     end_stop = get_stops(city, User(dest_latitude, dest_longitude, age), stop_limit=1)[0]
#     routes = get_routes(city)
#     find_route(city,start_stop, end_stop)
#
#     time = int(request.args.get('time', datetime.datetime.now()))
