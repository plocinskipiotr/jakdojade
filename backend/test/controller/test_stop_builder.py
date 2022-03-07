import pytest

from backend.src.controller.gps_coordinates_builder import GPSCoordinatesDirector
from backend.src.controller.stop import Stop
from backend.src.controller.stop_builder import StopStandardDirector, StopDBModelDirector


class TestStopStandardDirector:

    def test_director_happy_path(self):
        """Construct stop with correct data"""
        s = StopStandardDirector.construct(43, 'KSIĘŻE MAŁE',
                                           GPSCoordinatesDirector.construct(51.07784308, 17.08363569))
        assert isinstance(s, Stop)
        assert s.ID == 43
        assert s.name == 'KSIĘŻE MAŁE'
        assert s.gps_coordinates == GPSCoordinatesDirector.construct(51.07784308, 17.08363569)

    def test_director_no_args(self):
        """Construct stop without arguments"""
        with pytest.raises(TypeError):
            _ = StopStandardDirector.construct()


class TestStopDBModelDirector:

    def test_to_name(self):
        """Converting stop_id to stop_name"""
        ans = 'KRZYKI'
        data = ('KRZYKI',),
        it = iter(data)
        result = StopDBModelDirector.to_name(iter(data))
        assert ans == result
