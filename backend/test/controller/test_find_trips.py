import datetime

from backend.src.controller.closest_stops import closest_stops
from backend.src.controller.find_trips import find_trips
from backend.src.controller.trip import Trip
from backend.src.controller.user_builder import UserDirector
from backend.src.controller.stop_builder import StopDBModelDirector
from backend.src.model.db_queries import query_stops


class TestFindTrips:

    def test_find_trips(self):
        user = UserDirector.construct(51.10125726, 17.10914151, 25)
        target = UserDirector.construct(51.12250509, 17.03096835, 25)
        user_stop = closest_stops(user, query_stops(), stop_limit=1)[0]
        target_stop = closest_stops(target, query_stops(), stop_limit=1)[0]

        user_stop = StopDBModelDirector.construct(user_stop)
        target_stop = StopDBModelDirector.construct(target_stop)

        time = datetime.datetime.now().strftime('%H:%M:%S')
        trips = find_trips(user_stop, target_stop, time)
        assert isinstance(trips[0], Trip)
