import pytest

from backend.src.controller.find_departure import find_departure
from trips import trip_3_10000004
from stops import STOP_3144, STOP_4588


class TestFindDeparture:

    def test_happy_path(self):
        """Find departure for stop which exists in trip"""
        ans = '20:58:00'
        result = find_departure(trip_3_10000004, STOP_3144)
        assert result == ans

    def test_bad_path(self):
        """Find departure for stop which is not in trip timetable"""
        ans = '20:58:00'
        with pytest.raises(KeyError):
            _ = find_departure(trip_3_10000004, STOP_4588)

