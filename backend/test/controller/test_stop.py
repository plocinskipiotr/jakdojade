from backend.src.controller.gps_coordinates_builder import GPSCoordinatesDirector
from backend.src.controller.stop import Stop
from backend.src.controller.stop_builder import StopIDDirector


class TestStop:

    def test_stop(self):
        s =  StopIDDirector.construct(26)
        assert isinstance(s,Stop)
        assert s.ID == 26
        assert s.name == 'KSIĘŻE MAŁE'
        assert s.gps_coordinates == GPSCoordinatesDirector.construct(51.07784308,17.08363569)