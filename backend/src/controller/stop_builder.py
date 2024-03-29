"""This file contains stop builder class"""
import logging
from typing import Iterator

from deprecated import deprecated

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
        if not isinstance(ID, int):
            logging.warning('Error during Stop initiation: invalid ID')

        return self

    def with_name(self, name: str):
        self.stop.name = name

        if not isinstance(name, str):
            logging.warning('Error during Stop initiation: invalid name, stop id ' + str(self.stop.ID))

        return self

    def with_gps_coordinates(self, gps_coordinates: GPSCoordinates):
        self.stop.gps_coordinates = gps_coordinates

        if not isinstance(gps_coordinates, GPSCoordinates):
            logging.warning('Error during Stop initiation: invalid gps coordinates ' + str(self.stop.ID))

        return self

    def get_result(self):
        return self.stop


class StopStandardDirector:
    """Standard Stop Director, all fields must be filled"""

    @staticmethod
    def construct(ID: int, name: str, gps_coordinates: GPSCoordinates) -> Stop:
        """Builder construction method"""
        return StopBuilder() \
            .with_id(ID) \
            .with_name(name) \
            .with_gps_coordinates(gps_coordinates) \
            .get_result()


class StopDBModelDirector:
    """DBModel Director, only stop id is required, other required fields are queried from DB"""

    @staticmethod
    def construct(stop: Stops) -> Stop:
        """Builder construction method which use query result to build instance by DB Stop Model object"""
        return StopBuilder() \
            .with_id(stop.stop_id) \
            .with_name(StopDBModelDirector.to_name(query_stop_name(stop.stop_id))) \
            .with_gps_coordinates(GPSCoordinatesDirector.construct(stop.stop_lat, stop.stop_lon)) \
            .get_result()

    @staticmethod
    def to_name(iterator: Iterator[tuple]) -> str:
        """Converts query result to name"""
        el = list(iterator)
        return el[0][0]


@deprecated
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
