import pytest

from backend.src.controller.stop import GPSCoordinates
from backend.src.controller.stop_builder import GPSCoordinatesDirector


class TestGPSCoordinates:

    def test_director_happy_path(self):
        """Constructing object with correct data"""
        g = GPSCoordinatesDirector.construct(51.084062, 16.904824)
        assert isinstance(g, GPSCoordinates)
        assert g.latitude == 51.084062
        assert g.longitude == 16.904824

    def test_director_no_args(self):
        """Construct object without arguments (empty initiator)"""
        with pytest.raises(TypeError):
            _ = GPSCoordinatesDirector.construct()
