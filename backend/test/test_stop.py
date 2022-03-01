from backend.src.controller.stop import Stop


class TestStop:

    def test_stop(self):
        s = Stop('wroclaw', 357)
        assert isinstance(s,Stop)