"""
Contains function which can be used to find
trips from start stop to target stop.
The way it works:
    a) query all trips for start/target stop
    b) find which trips are common for both stops
    c) create trip object for common IDs
    d) filter trips in wrong direction (based on departure/arrival time)
"""

from backend.src.controller.stop import Stop
from backend.src.controller.trip import Trip
from backend.src.controller.trip_builder import TripSQLDirector
from backend.src.model.db_queries import query_trip_ids


def find_trips(start_stop: Stop, target_stop: Stop) -> set[Trip]:
    """find trips between two stops"""
    start_stop_trip_ids = query_trip_ids(start_stop.ID)
    target_stop_trips_ids = query_trip_ids(target_stop.ID)

    common_trip_ids = set(start_stop_trip_ids) & set(target_stop_trips_ids)
    trips = {TripSQLDirector.construct(ID[0]) for ID in common_trip_ids}
    trips = trips_on_target(trips, start_stop, target_stop)

    return trips


def trips_after_time(trips: set[Trip], start_stop: Stop, time: str) -> set[Trip]:
    """return trips with departure time after given time"""
    return {trip for trip in trips if trip.departure_time(start_stop) > time}


def trips_on_target(trips: set[Trip], start_stop: Stop, target_stop: Stop) -> set[Trip]:
    """return trips in proper direction (time of departure < time of arrival)"""
    return {trip for trip in trips if _valid_trip_direction(trip, start_stop, target_stop)}


def trip_by_arrival_time(trips: set[Trip], stop: Stop) -> list[Trip]:
    """sorts the trips by arrival time for determined stop"""
    return sorted(list(trips), key=lambda x: x.arrival_time(stop))


def _valid_trip_direction(trip: Trip, start_stop: Stop, target_stop: Stop) -> bool:
    """basing on time, decides if trip goes into right direction"""
    if trip.departure_time(start_stop) < trip.arrival_time(target_stop):
        return True
    else:
        return False
