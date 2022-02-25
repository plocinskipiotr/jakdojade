import heapq
import sqlalchemy
from flask import jsonify
from backend.src.constants import DB_CONF, POSTGRES
from backend.src.db_model import Cities
from backend.src.db_service import DBService
from backend.src.db_model import TableToClassParser
from geolocation import GeoPoint, Stop

db = DBService(DB_CONF, POSTGRES)
session_maker = db.get_sessionmaker()
session = session_maker()


def get_cities():
    result = session.query(Cities).all()
    result = [item.serialize() for item in result]
    result = jsonify(result)
    return result


def get_routes(city: str):
    result = session.query(TableToClassParser.parse(city)).all()
    result = [item.serialize() for item in result]
    result = jsonify(result)
    return result


def max_heap(ref_point: GeoPoint, stops: list[Stop], stop_limit=5):
    max_heap = list()
    for stop in stops:

        distance_to_stop = GeoPoint.calc_distance(ref_point, stop.geopoint)

        if len(max_heap) < stop_limit:
            heapq.heappush(max_heap, (-distance_to_stop, stop))
        elif distance_to_stop < -max_heap[0][0]:
            heapq.heapreplace(max_heap, (-distance_to_stop, stop))

    stops_by_distance = sorted(max_heap, key=lambda x: x[0], reverse=True)
    sorted_stops = [stop[1] for stop in stops_by_distance]
    return sorted_stops


def get_stops(city: str, latitude: float, longitude: float):
    user_point = GeoPoint(latitude, longitude)
    result = session.query(TableToClassParser.parse(city + '_stops')).all()
    result = [Stop(item.stop_id, item.stop_name, item.stop_lat, item.stop_lon) for item in result]
    result = max_heap(user_point, result)
    return result
