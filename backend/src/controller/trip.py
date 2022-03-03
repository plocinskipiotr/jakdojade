"""Represents single transports trip"""
from backend.src.controller.stop import Stop

timetable_record = [int, dict[str, str]]


class Trip:
    """Represents single transports trip"""

    def __init__(self):
        self.ID: str = ''
        self.stop_timetable: dict[timetable_record] = {}

    def arrival_time(self, stop: Stop) -> str:
        """return transport arrival time on stop"""
        return self.stop_timetable[stop.ID]['arrival']

    def departure_time(self, stop: Stop) -> str:
        """return transport departure time on stop"""
        return self.stop_timetable[stop.ID]['departure']

    def serialize(self) -> dict:
        """serialize instance attributes to dictionary"""
        return {'id': self.ID,
                'stop_timetables': self.stop_timetable
                }

    def __eq__(self, other):
        return self.ID == other.ID

    def __ne__(self, other):
        return self.ID != other.ID

    def __hash__(self):
        return int(self.ID)
