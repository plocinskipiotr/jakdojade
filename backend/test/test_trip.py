from backend.src.controller.trip import Trip
from backend.src.controller.trip_builder import TripSQLDirector


class TestTrip:

    def test_trip(self):
        t = TripSQLDirector.construct('wroclaw', '3_10090600')
        assert isinstance(t, Trip)
