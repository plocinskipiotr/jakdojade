"""This file contains serializers which change backend responses to json responses"""

from collections import namedtuple

from flask import jsonify

from backend.src.controller.stop import Stop
from backend.src.controller.trip import Trip

row = namedtuple('row', ['arrival', 'departure', 'name'])


def seek_closest_stops_serializer(stops: list[Stop] | list, point_lat: float, point_long: float):
    if len(stops) > 0:
        string = 'stops near ' + '(' + str(point_lat) + ',' + str(point_long) + ')'
        stops = [item.serialize() for item in stops]
        return jsonify({'msg': string, 'stops': stops})
    else:
        return no_stop_near_point(point_lat, point_long)


def no_stop_near_point(point_lat: float, point_long: float):
    return {'msg': 'There are no suitable stops near (' + str(point_lat) + ',' + str(point_long) + ')'}


def no_trip_between_stops(start_stop: Stop, target_stop: Stop):
    return {'msg': 'There are no suitable trip between stops',
            'start_stop': start_stop.serialize(),
            'target_stop': target_stop.serialize()}


def seek_departure_serializer(stop: Stop, dep_time: str, trip: Trip | None):
    if trip is not None:
        return jsonify({'stop': stop.serialize(),
                        'departure_time': dep_time,
                        'trip': trip_by_departure(trip).serialize()})
    else:
        return jsonify({'msg': 'There are no suitable departures from nearest stop',
                        'nearest stop': jsonify(stop.serialize())})


def trip_by_departure(trip: Trip):
    lst = []
    for k, v in trip.stop_timetable.items():
        item = (k, row(arrival=v['arrival'], departure=v['departure'], name=v['name']))
        lst.append(item)
    lst.sort(key=lambda x: x[1].departure)
    lst = [(item[0], {'name': item[1].name, 'arrival': item[1].arrival, 'departure': item[1].departure}) for item in
           lst]
    trip.stop_timetable = lst
    return trip
