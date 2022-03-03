from backend.src.controller.closest_stops import closest_stops
from backend.src.controller.stop_builder import StopDBModelDirector
from backend.src.controller.user_builder import UserDirector
from backend.src.model.db_kalisz import KaliszStops
from backend.src.model.db_wroclaw import WroclawStops


class TestClosestStops:

    def test_closest_stops_happy_path(self):
        stops = [
            WroclawStops(stop_id=1, stop_name='stop_1', stop_lat=23.231, stop_lon=17.21),
            WroclawStops(stop_id=2, stop_name='stop_3', stop_lat=23.233, stop_lon=17.21),
            WroclawStops(stop_id=3, stop_name='stop_2', stop_lat=23.232, stop_lon=17.21),
            WroclawStops(stop_id=4, stop_name='stop_5', stop_lat=23.235, stop_lon=17.21),
            WroclawStops(stop_id=5, stop_name='stop_4', stop_lat=23.234, stop_lon=17.21),
            WroclawStops(stop_id=6, stop_name='stop_7', stop_lat=23.237, stop_lon=17.21),
            WroclawStops(stop_id=7, stop_name='stop_6', stop_lat=23.236, stop_lon=17.21),
            WroclawStops(stop_id=8, stop_name='stop_8', stop_lat=23.239, stop_lon=17.21),
            WroclawStops(stop_id=9, stop_name='stop_7', stop_lat=23.238, stop_lon=17.21),
            WroclawStops(stop_id=10, stop_name='stop_10', stop_lat=23.240, stop_lon=17.21)
        ]

        u = UserDirector.construct(23.230, 17.21, 25)
        stops = [StopDBModelDirector.construct(stop) for stop in stops]
        res = closest_stops(u, stops)
        assert list(res) == [stops[0], stops[2], stops[1], stops[4], stops[3]]

    def test_closest_stops_too_away(self):
        stops = [
            WroclawStops(stop_id=1, stop_name='stop_1', stop_lat=30.231, stop_lon=17.21),
            WroclawStops(stop_id=2, stop_name='stop_2', stop_lat=30.232, stop_lon=17.21),
            WroclawStops(stop_id=3, stop_name='stop_3', stop_lat=30.233, stop_lon=17.21)
        ]

        u = UserDirector.construct(23.230, 17.21, 25)
        res = closest_stops(u, stops)
        assert list(res) == []

    def test_closest_stops_different_city(self):
        stops = [
            KaliszStops(stop_id=1, stop_name='stop_1', stop_lat=30.231, stop_lon=17.21),
            KaliszStops(stop_id=2, stop_name='stop_2', stop_lat=30.232, stop_lon=17.21),
            KaliszStops(stop_id=3, stop_name='stop_3', stop_lat=30.233, stop_lon=17.21)
        ]

        u = UserDirector.construct(30.230, 17.21, 25)
        res = closest_stops(u, stops)
        assert list(res) == [stops[0], stops[1], stops[2]]
