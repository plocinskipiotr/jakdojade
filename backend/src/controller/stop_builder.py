from typing import Iterator

from backend.src.controller.gps_coordinates import GPS_Coordinates
from backend.src.controller.gps_coordinates_builder import GPSCoordinatesDirector
from backend.src.controller.stop import Stop
from backend.src.controller.trip import Trip
from backend.src.controller.trip_builder import TripSQLDirector
from backend.src.model.db_queries import query_gps_coordinates, query_trip_ids, query_stop_name
from backend.src.model.db_base import Stops


class StopBuilder():

    def __init__(self):
        self.stop = Stop()

    def with_id(self, id: int):
        self.stop.id = id
        return self

    def with_name(self, name: str):
        self.stop.name = name
        return self

    def with_gps_coordinates(self, gps_coordinates: GPS_Coordinates):
        self.stop.gps_coordinates = gps_coordinates
        return self

    def with_trips(self, trips: set[Trip] | None):
        self.stop.trips = trips
        return self

    def get_result(self):
        return self.stop


class StopStandardDirector():

    @staticmethod
    def construct(id: int, name: str, gps_coordinates: GPS_Coordinates, trips: set[Trip]) -> Stop:
        return StopBuilder() \
            .with_id(id) \
            .with_name(name) \
            .with_gps_coordinates(gps_coordinates) \
            .with_trips(trips) \
            .get_result()


class StopIDDirector():

    @staticmethod
    def construct(id: int) -> Stop:
        return StopBuilder() \
            .with_id(id) \
            .with_name(StopIDDirector.to_name(query_stop_name(id))) \
            .with_gps_coordinates(StopIDDirector.to_gps_coordinates(query_gps_coordinates(id))) \
            .with_trips(to_set(query_trip_ids(id))) \
            .get_result()

    @staticmethod
    def to_gps_coordinates(iterator: Iterator[tuple]) -> GPS_Coordinates:
        single_point = list(iterator)[0]
        g = GPSCoordinatesDirector.construct(single_point[0], single_point[1])
        return g

    @staticmethod
    def to_name(iterator: Iterator[tuple]) -> str:
        el = list(iterator)
        return el[0][0]


class StopDBModelDirector():

    @staticmethod
    def construct(stop: Stops) -> Stop:
        return StopBuilder() \
            .with_id(stop.stop_id) \
            .with_name(StopIDDirector.to_name(query_stop_name(stop.stop_id))) \
            .with_gps_coordinates(GPSCoordinatesDirector.construct(stop.stop_lat, stop.stop_lon)) \
            .with_trips(to_set(query_trip_ids(stop.stop_id))) \
            .get_result()


def to_set(iterator: Iterator[tuple]) -> set[Trip]:
    trips = set()
    for el in iterator:
        trip = TripSQLDirector.construct(el[0])
        trips.add(trip)
    return trips
