from backend.src.controller.stop import Stop
from backend.src.controller.next_departure import next_departure


class TestNextDeparture:

    def test_next_departure(self):
        start = Stop('wroclaw', 1819, "21:37:00")
        end = Stop('wroclaw', 3488, "21:37:00")

        trip = next_departure(start, end)
        x = 'BREAK'