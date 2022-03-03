"""Builder for Trip class """
from typing import Iterator

from backend.src.controller.trip import Trip
from backend.src.model.db_queries import query_stop_time_tables


class TripBuilder:
    """Builder for Trip class """

    def __init__(self):
        self.trip = Trip()

    def with_id(self, ID: str):
        self.trip.ID = ID
        return self

    def with_stop_timetables(self, d: {int: tuple[str, str]}):
        self.trip.stop_timetable = d
        return self

    def get_result(self) -> Trip:
        return self.trip


class TripStandardDirector:

    @staticmethod
    def construct(ID: str, stop_time_tables: dict[int, dict[str, str]]) -> Trip:
        """Builder construction method"""
        return TripBuilder() \
            .with_id(ID) \
            .with_stop_timetables(stop_time_tables) \
            .get_result()


class TripSQLDirector:

    @staticmethod
    def construct(ID: str) -> Trip:
        """Builder construction method which query data from DB using trip ID"""
        return TripBuilder() \
            .with_id(ID) \
            .with_stop_timetables(TripSQLDirector.to_dict((query_stop_time_tables(ID)))) \
            .get_result()

    @staticmethod
    def to_dict(lst_iterator: Iterator[tuple]) -> dict:
        """Converts query result to dictionary"""
        d = {}
        for item in lst_iterator:
            stop, arrival, departure = item[0], item[1], item[2]
            d.update({stop: {'arrival': arrival, 'departure': departure}})
        return d
