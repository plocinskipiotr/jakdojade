from backend.src.controller.closest_stops import closest_stops, to_radius, distance_filter, HeapNode
from backend.src.controller.user_builder import UserDirector
from backend.src.controller.stop_builder import StopStandardDirector
from backend.src.controller.gps_coordinates_builder import GPSCoordinatesDirector
from stops import STOP_3144, STOP_4517


class TestClosestStops:

    def test_happy_path(self):
        """Checks 5 stops in user radius"""
        stops = [
            StopStandardDirector.construct(1, 'stop_1', GPSCoordinatesDirector.construct(23.232, 17.21)),
            StopStandardDirector.construct(2, 'stop_2', GPSCoordinatesDirector.construct(23.233, 17.21)),
            StopStandardDirector.construct(3, 'stop_3', GPSCoordinatesDirector.construct(23.234, 17.21)),
            StopStandardDirector.construct(4, 'stop_4', GPSCoordinatesDirector.construct(23.235, 17.21)),
            StopStandardDirector.construct(5, 'stop_5', GPSCoordinatesDirector.construct(23.236, 17.21))
        ]

        u = UserDirector.construct(23.230, 17.21, 25)
        res = closest_stops(u, stops)
        assert list(res) == [stops[0], stops[1], stops[2], stops[3], stops[4]]

    def test_out_of_radius(self):
        """Checks one stop out of user radius"""
        stops = [
            StopStandardDirector.construct(1, 'stop_1', GPSCoordinatesDirector.construct(23.292, 17.21))
        ]

        u = UserDirector.construct(23.230, 17.21, 25)
        res = closest_stops(u, stops)
        assert list(res) == []

    def test_no_stops(self):
        """Checks stops when no stops are provided"""
        stops = []

        u = UserDirector.construct(23.230, 17.21, 25)
        res = closest_stops(u, stops)
        assert list(res) == []

    def test_different_distance(self):
        """Returns 5 stops which are the close ones from user """
        stops = [
            StopStandardDirector.construct(1, 'stop_1', GPSCoordinatesDirector.construct(23.232, 17.21)),
            StopStandardDirector.construct(10, 'stop_10', GPSCoordinatesDirector.construct(23.241, 17.21)),
            StopStandardDirector.construct(2, 'stop_2', GPSCoordinatesDirector.construct(23.233, 17.21)),
            StopStandardDirector.construct(9, 'stop_9', GPSCoordinatesDirector.construct(23.240, 17.21)),
            StopStandardDirector.construct(3, 'stop_3', GPSCoordinatesDirector.construct(23.234, 17.21)),
            StopStandardDirector.construct(8, 'stop_8', GPSCoordinatesDirector.construct(23.239, 17.21)),
            StopStandardDirector.construct(4, 'stop_4', GPSCoordinatesDirector.construct(23.235, 17.21)),
            StopStandardDirector.construct(7, 'stop_7', GPSCoordinatesDirector.construct(23.238, 17.21)),
            StopStandardDirector.construct(5, 'stop_5', GPSCoordinatesDirector.construct(23.236, 17.21)),
            StopStandardDirector.construct(6, 'stop_6', GPSCoordinatesDirector.construct(23.237, 17.21)),
        ]

        u = UserDirector.construct(23.230, 17.21, 25)
        res = closest_stops(u, stops)
        assert list(res) == [stops[0], stops[2], stops[4], stops[6], stops[8]]


class TestDistanceFilter:

    def test_happy_path(self):
        """All nodes are in radius (no nodes filtered)"""
        ans = [HeapNode(4, STOP_3144), HeapNode(3, STOP_4517)]
        node_lst = [HeapNode(4, STOP_3144), HeapNode(3, STOP_4517)]
        node_lst = distance_filter(node_lst, 22)
        assert node_lst == ans

    def test_empty(self):
        """No nodes provided"""
        ans = []
        node_lst = []
        node_lst = distance_filter(node_lst, 22)
        assert node_lst == ans

    def test_filter(self):
        """One node filtered (too away from user), another passed"""
        ans = [HeapNode(3, STOP_4517)]
        node_lst = [HeapNode(10, STOP_3144), HeapNode(3, STOP_4517)]
        node_lst = distance_filter(node_lst, 22)
        assert node_lst == ans


class TestToRadius:

    def test_age_under_16(self):
        """Radio for user with age 15"""
        ans = 1
        result = to_radius(15)
        assert result == ans

    def test_age_between_16_25(self):
        """Radio for user with age 25"""
        ans = 5
        result = to_radius(25)
        assert result == ans

    def test_age_between_26_36(self):
        """Radio for user with age 35"""
        ans = 2
        result = to_radius(35)
        assert result == ans

    def test_age_between_36_51(self):
        """Radio for user with age 50"""
        ans = 1
        result = to_radius(50)
        assert result == ans

    def test_age_between_51_66(self):
        """Radio for user with age 65"""
        ans = 0.5
        result = to_radius(65)
        assert result == ans

    def test_age_over_66(self):
        """Radio for user with age 67"""
        ans = 0.1
        result = to_radius(67)
        assert result == ans
