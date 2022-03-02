from typing import Iterator

from backend.src.controller.gps_coordinates import GPS_Coordinates
from backend.src.controller.gps_coordinates_builder import GPSCoordinatesDirector
from backend.src.controller.stop import Stop
from backend.src.controller.trip import Trip
from backend.src.controller.trip_builder import TripSQLDirector
from backend.src.model.db_queries import query_geoloc, query_trip_ids


class StopBuilder():

    def __init__(self):
        self.stop = Stop()

    def with_city(self, city: str):
        self.stop.city = city
        return self

    def with_id(self, id: int):
        self.stop.id = id
        return self

    def with_gps_coordinates(self, gps_coordinates: GPS_Coordinates):
        self.stop.geopoint = gps_coordinates
        return self

    def with_trips(self, trips: set[Trip] | None):
        self.stop.trips = trips
        return self

    def get_result(self):
        return self.stop


class StopStandardDirector():

    @staticmethod
    def construct(city: str, id: int, gps_coordinates: GPS_Coordinates, trips: set[Trip]) -> Stop:
        return StopBuilder() \
            .with_city(city) \
            .with_id(id) \
            .with_gps_coordinates(gps_coordinates) \
            .with_trips(trips) \
            .get_result()


class StopSQLDirector():

    @staticmethod
    def construct(city: str, id: int) -> Stop:
        return StopBuilder() \
            .with_city(city) \
            .with_id(id) \
            .with_gps_coordinates(StopSQLDirector.to_gps_coordinates(query_geoloc(city, id))) \
            .with_trips(StopSQLDirector.to_set(city, query_trip_ids(city, id))) \
            .get_result()

    @staticmethod
    def to_gps_coordinates(iterator: Iterator[tuple]) -> GPS_Coordinates:
        single_point = list(iterator)[0]
        g = GPSCoordinatesDirector.construct(single_point[0], single_point[1])
        return g

    @staticmethod
    def to_set(city: str, iterator: Iterator[tuple]) -> set[Trip]:
        trips = set()
        for el in iterator:
            trip = TripSQLDirector.construct(city, el[0])
            trips.add(trip)
        return trips
