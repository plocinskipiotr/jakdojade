from backend.src.controller.stop import Stop
from backend.src.controller.trip import Trip


def find_departure(start_stop: Stop, target_stop: Stop, time: str) -> tuple[Stop, str]:
    trips = common_trips(start_stop, target_stop)
    trips = trips_at_time(trips, start_stop, time)
    trips = trips_on_target(trips, start_stop, target_stop)
    trips = list(trips)
    trips.sort(key=lambda trip: trip.arrival_time(target_stop.ID))
    return (start_stop, trips[0].departure_time(start_stop.ID))


def find_trips(start_stop: Stop, target_stop: Stop, time: str) -> list[Trip]:
    trips = common_trips(start_stop, target_stop)
    trips = trips_at_time(trips, start_stop, time)
    trips = trips_on_target(trips, start_stop, target_stop)
    trips = list(trips)
    trips.sort(key=lambda trip: trip.arrival_time(target_stop.ID))
    return trips


def common_trips(start_stop: Stop, target_stop: Stop) -> set[Trip]:
    """return trips which visits both stops"""
    return start_stop.trips & target_stop.trips


def trips_at_time(trips: set[Trip] | list[Trip], start_stop: Stop, time: str):
    """return trips after point of time"""
    return {trip for trip in trips if trip.departure_time(start_stop.ID) > time}


def trips_on_target(trips: set[Trip] | list[Trip], start_stop: Stop, target_stop: Stop):
    """return trips which fulfilled proper direction (time) condition"""
    return {trip for trip in trips if _valid_trip_direction(trip, start_stop.ID, target_stop.ID)}


def _valid_trip_direction(trip: Trip, start_id: int, end_id: int):
    if trip.departure_time(start_id) >= trip.arrival_time(end_id):
        return False
    else:
        return True
