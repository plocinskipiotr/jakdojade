from backend.src.controller.closest_stops import closest_stops
from backend.src.controller.user import User
from backend.src.model.db_kalisz import KaliszStops
from backend.src.model.db_wroclaw import WroclawStops


class TestClosestStops:

    def test_closest_stops_happy_path_wroclaw(self):
        stops = [
            WroclawStops(stop_id=1, stop_name='stop_1', stop_lat=23.231, stop_lon=17.21),
            WroclawStops(stop_id=2, stop_name='stop_2', stop_lat=23.232, stop_lon=17.21),
            WroclawStops(stop_id=3, stop_name='stop_3', stop_lat=23.233, stop_lon=17.21),
            WroclawStops(stop_id=4, stop_name='stop_4', stop_lat=23.234, stop_lon=17.21),
            WroclawStops(stop_id=5, stop_name='stop_5', stop_lat=23.235, stop_lon=17.21)
        ]

        user = User({'latitude': 23.230, 'longitude': 17.21}, 22)
        res = closest_stops(user, stops)
        assert res == [1, 2, 3, 4, 5]

    def test_closest_stops_happy_path_kalisz(self):
        stops = [
            KaliszStops(stop_id=1, stop_name='stop_1', stop_lat=23.231, stop_lon=17.21),
            KaliszStops(stop_id=2, stop_name='stop_2', stop_lat=23.232, stop_lon=17.21),
            KaliszStops(stop_id=3, stop_name='stop_3', stop_lat=23.233, stop_lon=17.21),
            KaliszStops(stop_id=4, stop_name='stop_4', stop_lat=23.234, stop_lon=17.21),
            KaliszStops(stop_id=5, stop_name='stop_5', stop_lat=23.235, stop_lon=17.21)
        ]

        user = User({'latitude': 23.230, 'longitude': 17.21}, 22)
        res = closest_stops(user, stops)
        assert res == [1, 2, 3, 4, 5]

    def test_not_in_radius(self):
        stops = [
            WroclawStops(stop_id=1, stop_name='stop_1', stop_lat=24.231, stop_lon=17.21),
            WroclawStops(stop_id=2, stop_name='stop_2', stop_lat=24.232, stop_lon=17.21),
            WroclawStops(stop_id=3, stop_name='stop_3', stop_lat=24.233, stop_lon=17.21),
            WroclawStops(stop_id=4, stop_name='stop_4', stop_lat=24.234, stop_lon=17.21),
            WroclawStops(stop_id=5, stop_name='stop_5', stop_lat=24.235, stop_lon=17.21)
        ]

        user = User({'latitude': 23.230, 'longitude': 17.21}, 22)
        res = closest_stops(user, stops)
        assert res == []

    def test_old_user(self):
        stops = [
            WroclawStops(stop_id=1, stop_name='stop_1', stop_lat=23.230, stop_lon=17.21),
            WroclawStops(stop_id=2, stop_name='stop_2', stop_lat=23.2301, stop_lon=17.21),
            WroclawStops(stop_id=3, stop_name='stop_3', stop_lat=23.242, stop_lon=17.21),
            WroclawStops(stop_id=4, stop_name='stop_4', stop_lat=23.243, stop_lon=17.21),
            WroclawStops(stop_id=5, stop_name='stop_5', stop_lat=23.244, stop_lon=17.21)
        ]

        user = User({'latitude': 23.230, 'longitude': 17.21}, 99)
        res = closest_stops(user, stops)
        assert res == [1, 2]
