from typing import Iterator

from flask import jsonify


def serialize_cities(cities: Iterator):
    cities = [item.serialize() for item in cities]
    cities = jsonify(cities)
    return cities


def serialize_routes(routes: Iterator):
    routes = [item.serialize() for item in routes]
    routes = jsonify(routes)
    return routes


def serialize_stops(stops: Iterator):
    stops = [item.serialize() for item in stops]
    stops = jsonify(stops)
    return stops
