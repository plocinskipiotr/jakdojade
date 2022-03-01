import datetime
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(ROOT_DIR))

from backend.src.model.db_queries import query_cities, query_routes, query_stops
from backend.src.view.view import serialize_cities, serialize_routes, serialize_stops

from flask import Flask, jsonify, request
from backend.src.controller.user import User
from backend.src.controller.closest_stops import closest_stops
from backend.src.controller.next_departure import next_departure

# db_init()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return jsonify(time=datetime.datetime.now())


@app.route('/public_transport/cities', methods=['GET'])
def cities():
    cities = query_cities()
    cities = serialize_cities(cities)
    return cities


@app.route('/public_transport/city/<string:city>/routes', methods=['GET'])
def city_routes(city):
    routes = query_routes(city)
    routes = serialize_routes(routes)
    return routes


@app.route('/public_transport/city/<string:city>/stop', methods=['GET'])
def closest_stop(city: str):
    u_lat = float(request.args.get('latitude'))
    u_long = float(request.args.get('longitude'))
    u_age = int(request.args.get('age', 25))
    u = User({'lat': u_lat, 'long': u_long}, u_age)

    stops = closest_stops(u, query_stops(city), stop_limit=5)
    stops = serialize_stops(stops)
    return stops


@app.route('/public_transport/city/<string:city>/next_departure', methods=['GET'])
def departure(city: str):
    user_lat = float(request.args.get('latitude'))
    user_long = float(request.args.get('longitude'))
    user_age = int(request.args.get('age', 25))
    user = User({'lat': user_lat, 'long': user_long}, user_age)

    end_lat = float(request.args.get('latitude'))
    end_long = float(request.args.get('longitude'))
    end = User({'lat': end_lat, 'long': end_long}, user_age)

    user_stop = closest_stops(user, query_stops(city), stop_limit=1)
    end_stop = closest_stops(end, query_stops(city), stop_limit=1)

    x = next_departure(list(user_stop)[0], list(end_stop)[0])
    return x
