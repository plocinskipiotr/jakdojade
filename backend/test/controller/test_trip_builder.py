import pytest

from backend.src.controller.trip import Trip
from backend.src.controller.trip_builder import TripStandardDirector, TripSQLDirector
from trips import STOP_TIMETABLE_TRIP_3_10000000


class TestTripStandardDirector:

    def test_director_happy_path(self):
        """Constructing trip with correct data"""
        t = TripStandardDirector.construct('3_10000000', STOP_TIMETABLE_TRIP_3_10000000)
        assert isinstance(t, Trip)
        assert t.ID == '3_10000000'
        assert t.stop_timetable == STOP_TIMETABLE_TRIP_3_10000000

    def test_director_empty_timetable(self):
        """Constructing trip with empty timetable"""
        t = TripStandardDirector.construct('3_10000000', {})
        assert isinstance(t, Trip)
        assert t.ID == '3_10000000'
        assert t.stop_timetable == {}

    def test_director_no_args(self):
        """Constructing trip without arguments"""
        with pytest.raises(TypeError):
            t = TripStandardDirector.construct()


class TestTripSQLDirector:

    def test_to_dict(self):
        """Parsing sql query to timetable format"""
        ans = {4739: {'name': 'KRZYKI', 'arrival': '22:31:00', 'departure': '22:31:00'}}
        data = (4739, 'KRZYKI', '22:31:00', '22:31:00'),
        it = iter(data)
        result = TripSQLDirector.to_timetable(it)
        assert result == ans
