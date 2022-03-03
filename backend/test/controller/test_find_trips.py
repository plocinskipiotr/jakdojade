import datetime

from backend.src.controller.closest_stops import closest_stops
from backend.src.controller.find_trips import find_trips
from backend.src.controller.stop_builder import StopDBModelDirector
from backend.src.controller.trip import Trip
from backend.src.controller.user_builder import UserDirector
from backend.src.model.db_queries import query_stops


class TestFindTrips:

    def test_find_trips(self):
        user = UserDirector.construct(51.078074, 16.9982022, 25)
        target = UserDirector.construct(51.10585896, 17.04334082, 25)
        time = datetime.datetime.now().strftime('%H:%M:%S')
        stops = [StopDBModelDirector.construct(stop) for stop in query_stops('wroclaw')]
        user_stop = closest_stops(user, stops, stop_limit=1)[0]
        target_stop = closest_stops(target, stops, stop_limit=1)[0]
        trips = list(find_trips(user_stop, target_stop, time))
        assert isinstance(trips[0], Trip)
