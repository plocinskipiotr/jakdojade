"""This file contains Trip Builder class"""
import logging
from typing import Iterator

from backend.src.controller.trip import Trip, timetable
from backend.src.model.db_queries import query_stop_time_tables


class TripBuilder:
    """Builder for Trip class """

    def __init__(self):
        self.trip = Trip()

    def with_id(self, ID: str):
        self.trip.ID = ID

        if ID is None or len(ID) == 0:
            logging.warning('Error during Trip initiation: invalid ID')

        return self

    def with_stop_timetable(self, d: timetable):
        self.trip.stop_timetable = d

        if not isinstance(d, dict):
            logging.warning('Error during Trip initiation: invalid timetable, trip id: ' + self.trip.ID)
        return self

    def get_result(self) -> Trip:
        return self.trip


class TripStandardDirector:

    @staticmethod
    def construct(ID: str, stop_time_table: timetable) -> Trip:
        """Builder construction method"""
        return TripBuilder() \
            .with_id(ID) \
            .with_stop_timetable(stop_time_table) \
            .get_result()


class TripSQLDirector:

    @staticmethod
    def construct(ID: str) -> Trip:
        """Builder construction method which query data from DB using trip ID"""
        return TripBuilder() \
            .with_id(ID) \
            .with_stop_timetable(TripSQLDirector.to_timetable(query_stop_time_tables(ID))) \
            .get_result()

    @staticmethod
    def to_timetable(lst_iter: Iterator[tuple]) -> dict:
        """Converts query result to dictionary"""
        d = {}
        for item in lst_iter:
            stop_id, stop_name, arrival, departure = item[0], item[1], item[2], item[3]
            d.update({stop_id: {'name': stop_name, 'arrival': arrival, 'departure': departure}})
        return d
