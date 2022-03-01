import heapq
from collections import namedtuple
from typing import Iterator

from backend.src.model import db_base
from backend.src.controller.geolocation import GeoPoint
from backend.src.controller.user import User

Node = namedtuple('Node', ['distance', 'stop'])


def closest_stops(user: User, stops: list[db_base.Stops], stop_limit=5) -> Iterator:
    def distance_filter(max_heap: list[Node], age: int):
        return list(filter(lambda x: abs(x.distance) < to_radius(age), max_heap))

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

    max_heap = list()

    for stop in stops:
        stop_geopoint = GeoPoint({'lat': stop.stop_lat, 'long': stop.stop_lon})
        distance_to_stop = user.geopoint.calc_distance(stop_geopoint)
        node = Node(-distance_to_stop, stop)

        if len(max_heap) < stop_limit:
            heapq.heappush(max_heap, node)
        elif distance_to_stop < -max_heap[0].distance:
            heapq.heapreplace(max_heap, node)

    node_lst = distance_filter(max_heap, user.age)
    node_lst = sorted(node_lst, key=lambda x: x.distance, reverse=True)
    stop_lst = [node.stop for node in node_lst]

    return iter(stop_lst)
