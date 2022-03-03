from typing import Iterator, List

from backend.src.controller.gpscoordinates import GPSCoordinates
from backend.src.controller.gps_coordinates_builder import GPSCoordinatesDirector
from backend.src.controller.stop import Stop
from backend.src.model.db_queries import query_gps_coordinates, query_stop_name
from backend.src.model.db_model import Stops


class StopBuilder:

    def __init__(self):
        self.stop = Stop()

    def with_id(self, id: int):
        self.stop.ID = id
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
        return StopBuilder() \
            .with_id(ID) \
            .with_name(name) \
            .with_gps_coordinates(gps_coordinates) \
            .get_result()


class StopIDDirector:

    @staticmethod
    def construct(ID: int) -> Stop:
        return StopBuilder() \
            .with_id(ID) \
            .with_name(StopIDDirector.to_name(query_stop_name(ID))) \
            .with_gps_coordinates(StopIDDirector.to_gps_coordinates(query_gps_coordinates(ID))) \
            .get_result()

    @staticmethod
    def to_gps_coordinates(iterator: Iterator[tuple]) -> GPSCoordinates:
        single_point = list(iterator)[0]
        g = GPSCoordinatesDirector.construct(single_point[0], single_point[1])
        return g

    @staticmethod
    def to_name(iterator: Iterator[tuple]) -> str:
        el = list(iterator)
        return el[0][0]


class StopDBModelDirector:

    @staticmethod
    def construct(stop: Stops) -> Stop:
        return StopBuilder() \
            .with_id(stop.stop_id) \
            .with_name(StopIDDirector.to_name(query_stop_name(stop.stop_id))) \
            .with_gps_coordinates(GPSCoordinatesDirector.construct(stop.stop_lat, stop.stop_lon)) \
            .get_result()
