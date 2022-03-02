import datetime

from backend.src.controller.next_departure import next_departure
from backend.src.controller.user_builder import UserDirector
from backend.src.model.db_queries import query_stops


class TestNextDeparture:

    def test_next_departure(self):
        user = UserDirector.construct(51.10125726, 17.10914151, 25)
        target = UserDirector.construct(51.12250509, 17.03096835, 25)
        time = datetime.datetime.now().strftime('%H:%M:%S')
        departure = next_departure('wroclaw', time, user, target, query_stops('wroclaw'))
        x = 'BREAK'
