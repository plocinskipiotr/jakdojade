from typing import Iterator

from flask import jsonify

from backend.src.controller.stop import Stop
from backend.src.controller.trip import Trip
from backend.src.model.db_base import Stops


def serialize_cities(cities: Iterator):
    cities = [item.serialize() for item in cities]
    cities = jsonify(cities)
    return cities


def serialize_routes(routes: Iterator):
    routes = [item.serialize() for item in routes]
    routes = jsonify(routes)
    return routes


def serialize_stops(stops: list[Stops]):
    stops = [item.serialize() for item in stops]
    stops = jsonify(stops)
    return stops


def serialize_trips(trips: list[Trip]):
    trips = [item.serialize() for item in trips]
    trips = jsonify(trips)
    return trips


def serialize_departure(departure: tuple[Stop, str]):
    dep0 = departure[0].serialize()
    dep1 = {'departure_time': departure[1]}
    lst = [dep0, dep1]
    dep = jsonify(lst)
    return dep
