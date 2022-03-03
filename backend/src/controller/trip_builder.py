from typing import Iterator

from backend.src.controller.trip import Trip
from backend.src.model.db_queries import query_stop_time_tables


class TripBuilder():

    def __init__(self):
        self.trip = Trip()

    def with_id(self, id: str):
        self.trip.id = id
        return self

    def with_stop_timetables(self, dict: {int: tuple[str, str]}):
        self.trip.stop_timetables = dict
        return self

    def get_result(self) -> Trip:
        return self.trip


class TripSQLDirector():

    @staticmethod
    def construct(id: str) -> Trip:
        return TripBuilder() \
            .with_id(id) \
            .with_stop_timetables(TripSQLDirector.to_dict(query_stop_time_tables(id))) \
            .get_result()

    @staticmethod
    def to_dict(lst_iterator: Iterator[tuple]):
        d = {}
        for item in lst_iterator:
            stop, arrival, departure = item[0], item[1], item[2]
            d.update({stop: {'arrival': arrival, 'departure': departure}})
        return d


class TripStandardDirector():

    @staticmethod
    def construct(id: str, stop_time_tables: dict[str, tuple[str, str]]) -> Trip:
        return TripBuilder() \
            .with_id(id) \
            .with_stop_timetables(stop_time_tables) \
            .get_result()
