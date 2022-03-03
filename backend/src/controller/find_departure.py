"""
Contains function which can be used to find
departure time from start stop to target stop.
Departure time is based on  earliest arrival at
the target stop
    return: departure time (str)
"""

from backend.src.controller.find_trips import find_trips
from backend.src.controller.stop import Stop


def find_departure(start_stop: Stop, target_stop: Stop, time: str) -> str:
    """find next departure from stop to target after given time"""
    trips = find_trips(start_stop, target_stop, time)
    try:
        trip = sorted(trips, key=lambda item: item.arrival_time(target_stop))[0]
    except IndexError:
        return 'There is no suitable trip found'
    departure_time = trip.departure_time(start_stop)
    return departure_time
