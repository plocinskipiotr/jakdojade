import heapq
from collections import namedtuple
from backend.src.model import db_base
from backend.src.controller.gps_coordinates import GPS_Coordinates
from backend.src.controller.gps_coordinates_builder import GPSCoordinatesDirector
from backend.src.controller.user import User

HeapNode = namedtuple('Node', ['distance', 'stop'])


def closest_stops(user: User, stops: list[db_base.Stops], stop_limit=5) -> list[db_base.Stops]:
    def distance_filter(max_heap: list[HeapNode], age: int):
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

    def root(heap: list) -> HeapNode:
        return heap[0]

    max_heap = list()

    for stop in stops:

        user_coordinates = user.gps_coordinates
        stop_coordinates = GPSCoordinatesDirector.construct(stop.stop_lat, stop.stop_lon)

        distance = GPS_Coordinates.calc_distance(user_coordinates, stop_coordinates)
        node = HeapNode(-distance, stop)

        if len(max_heap) < stop_limit:
            heapq.heappush(max_heap, node)
        elif distance < -root(max_heap).distance:
            heapq.heapreplace(max_heap, node)

    node_lst = distance_filter(max_heap, user.age)
    node_lst = sorted(node_lst, key=lambda x: x.distance, reverse=True)
    stop_lst = [node.stop for node in node_lst]

    return stop_lst
