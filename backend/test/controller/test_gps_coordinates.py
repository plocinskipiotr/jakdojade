from backend.src.controller.stop import GPS_Coordinates
from backend.src.controller.stop_builder import GPSCoordinatesDirector


class TestGeopoint:

    def test_geopoint(self):
        g = GPSCoordinatesDirector.construct(51.084062, 16.904824)
        assert isinstance(g, GPS_Coordinates)
