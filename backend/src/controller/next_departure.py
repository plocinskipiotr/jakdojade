from backend.src.controller.stop import Stop
from backend.src.controller.trip import Trip


def next_departure(start_stop: Stop, end_stop: Stop) -> Trip:
    all_trips = start_stop.trips & end_stop.trips
    trips = [trip for trip in all_trips if
             valid_trip_direction(trip, start_stop, end_stop)]
    trips.sort(key=lambda x: x.stops_arrival[end_stop.stop_id])
    return trips[0].stops_departure[start_stop.stop_id]


def valid_trip_direction(trip: Trip, start: Stop, end: Stop):
    if trip.stops_departure[start.stop_id] >= trip.stops_departure[end.stop_id]:
        return False
    else:
        return True
