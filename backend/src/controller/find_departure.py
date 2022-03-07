"""
find next departure from stop for trip
    return: departure time (str)
"""
from backend.src.controller.stop import Stop
from backend.src.controller.trip import Trip


def find_departure(trip: Trip, stop: Stop) -> str:
    """find next departure from stop for trip"""
    departure_time = trip.departure_time(stop)
    return departure_time
