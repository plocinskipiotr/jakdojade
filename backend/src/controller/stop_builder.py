"""Builder for stop class """
from typing import Iterator

from backend.src.controller.gpscoordinates import GPSCoordinates
from backend.src.controller.gps_coordinates_builder import GPSCoordinatesDirector
from backend.src.controller.stop import Stop
from backend.src.model.db_queries import query_gps_coordinates, query_stop_name
from backend.src.model.db_model import Stops


class StopBuilder:
    """Builder for stop class """

    def __init__(self):
        self.stop = Stop()

    def with_id(self, ID: int):
        self.stop.ID = ID
        return self

    def with_name(self, name: str):
        self.stop.name = name
        return self

    def with_gps_coordinates(self, gps_coordinates: GPSCoordinates):
        self.stop.gps_coordinates = gps_coordinates
        return self

    def get_result(self):
        return self.stop


class StopStandardDirector:

    @staticmethod
    def construct(ID: int, name: str, gps_coordinates: GPSCoordinates) -> Stop:
        """Builder construction method"""
        return StopBuilder() \
            .with_id(ID) \
            .with_name(name) \
            .with_gps_coordinates(gps_coordinates) \
            .get_result()


class StopIDDirector:

    @staticmethod
    def construct(ID: int) -> Stop:
        """Builder construction method which use query result to build instance by stop id"""
        return StopBuilder() \
            .with_id(ID) \
            .with_name(StopIDDirector.to_name(query_stop_name(ID))) \
            .with_gps_coordinates(StopIDDirector.to_gps_coordinate(query_gps_coordinates(ID))) \
            .get_result()

    @staticmethod
    def to_gps_coordinate(iterator: Iterator[tuple]) -> GPSCoordinates:
        """Converts query result to GPS Coordinates object"""
        single_point = list(iterator)[0]
        g = GPSCoordinatesDirector.construct(single_point[0], single_point[1])
        return g

    @staticmethod
    def to_name(iterator: Iterator[tuple]) -> str:
        """Converts query result to name"""
        el = list(iterator)
        return el[0][0]


class StopDBModelDirector:

    @staticmethod
    def construct(stop: Stops) -> Stop:
        """Builder construction method which use query result to build instance by DB Stop Model object"""
        return StopBuilder() \
            .with_id(stop.stop_id) \
            .with_name(StopIDDirector.to_name(query_stop_name(stop.stop_id))) \
            .with_gps_coordinates(GPSCoordinatesDirector.construct(stop.stop_lat, stop.stop_lon)) \
            .get_result()
