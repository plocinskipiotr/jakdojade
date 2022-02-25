import heapq
from collections import namedtuple

from backend.src.db_model import Stops
from backend.src.geolocation import GeoPoint
from backend.src.user import User

Node = namedtuple('Node', ['distance', 'stop'])


def to_radius(age: int) -> float:
    if age < 16:
        return 1
    elif age < 26:
        return 5
    elif age < 36:
        return 2
    elif age < 51:
        return 1
    elif age < 66:
        return 0.5
    else:
        return 0.1


def find_closest_stops(user: User, stops: list[Stops], stop_limit=5):
    max_heap = list()

    for stop in stops:
        stop_geopoint = GeoPoint(stop.stop_lat, stop.stop_lon)
        distance_to_stop = user.geopoint.calc_distance(stop_geopoint)
        node = Node(-distance_to_stop, stop)

        if len(max_heap) < stop_limit:
            heapq.heappush(max_heap, node)
        elif distance_to_stop < -max_heap[0].distance:
            heapq.heapreplace(max_heap, node)

    stops = distance_filter(max_heap, user.age)
    stops = sorted(stops, key=lambda x: x.distance, reverse=True)
    stops = [item.stop for item in stops]

    return stops


def distance_filter(max_heap: list[Node], age: int):
    return list(filter(lambda x: abs(x.distance) < to_radius(age), max_heap))
