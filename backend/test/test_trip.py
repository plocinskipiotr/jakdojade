from backend.src.controller.trip import Trip


class TestTrip:

    def test_trip(self):
        t = Trip('wroclaw', '3_10090600')
        assert isinstance(t,Trip)