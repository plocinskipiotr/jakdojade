"""This file contains Trip class which represents bus/tram trip
Trip starts at some stop and end the journey at some :)
"""
from backend.src.controller.stop import Stop

timetable_record = [int, dict[str, str, str]]
timetable = dict[timetable_record]


class Trip:
    """Represents single transports trip"""

    def __init__(self):
        self.ID: str = ''
        self.stop_timetable: timetable = {}

    def arrival_time(self, stop: Stop) -> str:
        """return transport arrival time on stop"""
        return self.stop_timetable[stop.ID]['arrival']

    def departure_time(self, stop: Stop) -> str:
        """return transport departure time on stop"""
        try:
            return self.stop_timetable[stop.ID]['departure']
        except KeyError:
            raise KeyError('There is no stop id ' + str(stop.ID) + ' in trip ' + self.ID + ' timetable')

    def serialize(self) -> dict:
        """serialize instance attributes to dictionary"""
        return {'trip ID': self.ID,
                'stop_timetable': self.stop_timetable
                }

    def __eq__(self, other):
        return self.ID == other.ID

    def __ne__(self, other):
        return self.ID != other.ID

    def __hash__(self):
        return int(self.ID)
