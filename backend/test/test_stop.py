from backend.src.controller.stop import Stop
from backend.src.controller.stop_builder import StopSQLDirector

class TestStop:

    def test_stop(self):
        s =  StopSQLDirector.construct('wroclaw',26)
        assert isinstance(s,Stop)