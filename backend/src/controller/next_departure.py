from typing import Any

from backend.src.controller.stop import Stop
from backend.src.controller.trip import Trip
from backend.src.controller.closest_stops import closest_stops
from backend.src.controller.user import User
from backend.src.controller.stop_builder import StopDBModelDirector
from backend.src.model.db_base import Stops


def next_departure(city: str, time: str, user: User, target: User, stops: Stops) -> str | tuple[Stop, Any]:
    start_stop = closest_stops(user, stops, stop_limit=1)[0]
    target_stop = closest_stops(target, stops, stop_limit=1)[0]

    start_stop = StopDBModelDirector.construct(city, start_stop)
    target_stop = StopDBModelDirector.construct(city, target_stop)

    common_trips = start_stop.trips & target_stop.trips
    trips_on_target = [trip for trip in common_trips if
                       valid_trip_direction(trip, start_stop.id, target_stop.id)]

    trips = [trip for trip in trips_on_target if trip.departure_time_by_stop_id(start_stop.id) > time]

    trips.sort(key=lambda x: x.arrival_time_by_stop_id(target_stop.id))
    time = trips[0].departure_time_by_stop_id(start_stop.id)
    return (start_stop, time)


def valid_trip_direction(trip: Trip, start_id: int, end_id: int):
    if trip.departure_time_by_stop_id(start_id) >= trip.arrival_time_by_stop_id(end_id):
        return False
    else:
        return True
