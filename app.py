import datetime
from flask import Flask, jsonify, request
from settings import ROOT_DIR
from backend.src.controller.find_trips import find_trips, trips_after_time, trip_by_arrival_time
from backend.src.controller.find_departure import find_departure
from backend.src.controller.validate_path import validate_path
from backend.src.controller.user_builder import UserDirector
from backend.src.controller.stop_builder import StopDBModelDirector
from backend.src.controller.closest_stops import closest_stops
from backend.src.view.view import trip_by_departure, seek_closest_stops_serializer, seek_departure_serializer, \
    no_stop_near_point, no_trip_between_stops
from backend.src.migration.db_init import db_init
from backend.src.model.db_queries import query_cities, query_routes, query_stops

validate_path(ROOT_DIR)
db_init()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return jsonify(time=datetime.datetime.now())


@app.route('/public_transport/cities', methods=['GET'])
def cities():
    iterator = query_cities()
    lst = jsonify([item.serialize() for item in iterator])
    return lst


@app.route('/public_transport/city/<string:city>/routes', methods=['GET'])
def city_routes(city):
    iterator = query_routes(city)
    lst = jsonify([item.serialize() for item in iterator])
    return lst


@app.route('/public_transport/city/<string:city>/find_trips', methods=['GET'])
def seek_trips(city: str):
    user_lat = float(request.args.get('u_lat'))
    user_long = float(request.args.get('u_long'))
    user_age = int(request.args.get('age', 25))
    user = UserDirector.construct(user_lat, user_long, user_age)

    target_lat = float(request.args.get('t_lat'))
    target_long = float(request.args.get('t_long'))
    target = UserDirector.construct(target_lat, target_long, user_age)

    time = str(request.args.get('time', datetime.datetime.now().strftime('%H:%M:%S')))

    stops = [StopDBModelDirector.construct(stop) for stop in query_stops(city)]

    user_stop = closest_stops(user, stops, stop_limit=1)[0]
    target_stop = closest_stops(target, stops, stop_limit=1)[0]

    trips = find_trips(user_stop, target_stop)
    trips = trips_after_time(trips, user_stop, time)
    trips = jsonify([trip_by_departure(trip).serialize() for trip in trips])

    return trips


@app.route('/public_transport/city/<string:city>/stop', methods=['GET'])
def seek_closest_stops(city: str):
    u_lat = float(request.args.get('latitude'))
    u_long = float(request.args.get('longitude'))
    u_age = int(request.args.get('age', 25))

    user = UserDirector.construct(u_lat, u_long, u_age)
    stops = [StopDBModelDirector.construct(stop) for stop in query_stops(city)]
    stops = closest_stops(user, stops, stop_limit=5)

    response = seek_closest_stops_serializer(stops, u_lat, u_long)
    return response


@app.route('/public_transport/city/<string:city>/departure', methods=['GET'])
def seek_departure(city: str):
    user_lat = float(request.args.get('u_lat'))
    user_long = float(request.args.get('u_long'))
    user_age = int(request.args.get('age', 25))
    target_lat = float(request.args.get('t_lat'))
    target_long = float(request.args.get('t_long'))
    time = str(request.args.get('time', datetime.datetime.now().strftime('%H:%M:%S')))

    user = UserDirector.construct(user_lat, user_long, user_age)
    target = UserDirector.construct(target_lat, target_long, user_age)
    stops = [StopDBModelDirector.construct(stop) for stop in query_stops(city)]

    try:
        user_stop = closest_stops(user, stops, stop_limit=1)[0]
    except IndexError:
        return no_stop_near_point(user_lat, user_long)

    try:
        target_stop = closest_stops(target, stops, stop_limit=1)[0]
    except IndexError:
        return no_stop_near_point(target_lat, target_long)

    trips = find_trips(user_stop, target_stop)
    trips = trips_after_time(trips, user_stop, time)

    try:
        trip = trip_by_arrival_time(trips, target_stop)[0]
    except IndexError:
        return no_trip_between_stops(user_stop, target_stop)

    dep_time = find_departure(trip, user_stop)
    response = seek_departure_serializer(user_stop, dep_time, trip)
    return response
