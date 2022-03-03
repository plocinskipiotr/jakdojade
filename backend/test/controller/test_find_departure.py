import datetime

from backend.src.controller.closest_stops import closest_stops
from backend.src.controller.find_departure import find_departure
from backend.src.controller.user_builder import UserDirector
from backend.src.controller.stop_builder import StopDBModelDirector
from backend.src.model.db_queries import query_stops


class TestFindDeparture:

    def test_find_departure(self):
        user = UserDirector.construct(51.10125726, 17.10914151, 25)
        target = UserDirector.construct(51.12250509, 17.03096835, 25)
        time = '00:00:00'
        stops = [StopDBModelDirector.construct(stop) for stop in query_stops('wroclaw')]
        user_stop = closest_stops(user, stops, stop_limit=1)[0]
        target_stop = closest_stops(target, stops, stop_limit=1)[0]
        departure = find_departure(user_stop, target_stop, time)

        x = 'BREAK'
