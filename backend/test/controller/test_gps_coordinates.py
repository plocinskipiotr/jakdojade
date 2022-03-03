from backend.src.controller.stop import GPSCoordinates
from backend.src.controller.stop_builder import GPSCoordinatesDirector


class TestGeopoint:

    def test_geopoint(self):
        g = GPSCoordinatesDirector.construct(51.084062, 16.904824)
        assert isinstance(g, GPSCoordinates)
        assert g.latitude == 51.084062
        assert g.longitude == 16.904824
