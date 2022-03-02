from backend.src.controller.stop import Stop
from backend.src.controller.stop_builder import StopIDDirector

class TestStop:

    def test_stop(self):
        s =  StopIDDirector.construct('wroclaw', 26)
        assert isinstance(s,Stop)