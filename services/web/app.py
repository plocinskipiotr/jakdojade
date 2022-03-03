import datetime
import sys

from backend.settings import ROOT_DIR

sys.path.append(str(ROOT_DIR))
from backend.src.migration.db_init import db_init
from backend.src.controller.stop_builder import StopDBModelDirector
from backend.src.model.db_queries import query_cities, query_routes, query_stops
from backend.src.view.view import serialize_cities, serialize_routes, serialize_stops, serialize_trips, \
    serialize_departure
from backend.src.controller.user_builder import UserDirector
from flask import Flask, jsonify, request
from backend.src.controller.closest_stops import closest_stops
from backend.src.controller.find_trips import find_trips, find_departure

db_init()

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
def seek_closest_stops(city: str):
    u_lat = float(request.args.get('latitude'))
    u_long = float(request.args.get('longitude'))
    u_age = int(request.args.get('age', 25))

    user = UserDirector.construct(u_lat, u_long, u_age)
    stops = closest_stops(user, query_stops(city), stop_limit=5)
    stops = serialize_stops(stops)
    return stops


@app.route('/public_transport/city/<string:city>/find_trips', methods=['GET'])
def seek_trips(city: str):
    user_lat = float(request.args.get('u_lat'))
    user_long = float(request.args.get('u_long'))
    user_age = int(request.args.get('age', 25))
    user = UserDirector.construct(user_lat, user_long, user_age)

    target_lat = float(request.args.get('t_lat'))
    target_long = float(request.args.get('t_long'))
    target = UserDirector.construct(target_lat, target_long, user_age)

    user_stop = closest_stops(user, query_stops(city), stop_limit=1)[0]
    target_stop = closest_stops(target, query_stops(city), stop_limit=1)[0]
    user_stop = StopDBModelDirector.construct(user_stop)
    target_stop = StopDBModelDirector.construct(target_stop)

    time = datetime.datetime.now().strftime('%H:%M:%S')
    trips = find_trips(user_stop, target_stop, time)
    trips = serialize_trips(trips)

    return trips


@app.route('/public_transport/city/<string:city>/departure', methods=['GET'])
def seek_departure(city: str):
    user_lat = float(request.args.get('u_lat'))
    user_long = float(request.args.get('u_long'))
    user_age = int(request.args.get('age', 25))
    user = UserDirector.construct(user_lat, user_long, user_age)

    target_lat = float(request.args.get('t_lat'))
    target_long = float(request.args.get('t_long'))
    target = UserDirector.construct(target_lat, target_long, user_age)

    user_stop = closest_stops(user, query_stops(city), stop_limit=1)[0]
    target_stop = closest_stops(target, query_stops(city), stop_limit=1)[0]
    user_stop = StopDBModelDirector.construct(user_stop)
    target_stop = StopDBModelDirector.construct(target_stop)

    time = datetime.datetime.now().strftime('%H:%M:%S')
    trips = find_departure(user_stop, target_stop, time)
    departure = serialize_departure(trips)

    return departure
