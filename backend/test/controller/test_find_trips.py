from unittest.mock import patch

from backend.src.controller.find_trips import find_trips, _valid_trip_direction, trips_after_time, trips_on_target, \
    trip_by_arrival_time
from backend.src.controller.trip_builder import TripStandardDirector
from backend.test.controller.stops import STOP_3144, STOP_4517
from backend.test.controller.trips import trip_3_10000002, trip_3_10000003, \
    trip_3_10000004, STOP_TIMETABLE_TRIP_3_10000004, STOP_TIMETABLE_TRIP_3_10000003


class TestValidTripDirection:

    def test_departure_before_arrival(self):
        """Departure is earlier as arrival"""""
        ans = True
        result = _valid_trip_direction(trip_3_10000003, STOP_3144, STOP_4517)
        assert ans == result

    def test_departure_after_arrival(self):
        """Departure is later as arrival"""
        ans = False
        result = _valid_trip_direction(trip_3_10000003, STOP_4517, STOP_3144)
        assert ans == result


class TestTripsAfterTime:
    """Filter function that checks if only trips that occurs after given time-point go through"""

    def test_happy_path(self):
        """All trips fulfilled condition"""
        ans = {trip_3_10000002, trip_3_10000003}
        trip_set = {trip_3_10000002, trip_3_10000003}
        trips = trips_after_time(trip_set, STOP_3144, '20:00:00')
        assert trips == ans

    def test_no_trip(self):
        """Empty set of trips"""
        ans = set()
        trip_set = set()
        trips = trips_after_time(trip_set, STOP_3144, '00:00:00')
        assert trips == ans

    def test_trip_filtered(self):
        """One trip fulfilled condition"""
        ans = {trip_3_10000003}
        trip_set = {trip_3_10000002, trip_3_10000003}
        trips = trips_after_time(trip_set, STOP_3144, '20:30:00')
        assert trips == ans


class TestTripsOnTarget:
    """This function checks if condition 'departure before arrival' is fulfilled by trip"""

    def test_trips_on_target(self):
        """All trips fulfilled should pass"""
        ans = {trip_3_10000002, trip_3_10000003}
        trip_set = {trip_3_10000002, trip_3_10000003}
        trips = trips_on_target(trip_set, STOP_3144, STOP_4517)
        assert trips == ans

    def test_no_trips(self):
        """No trips provided"""
        ans = set()
        trip_set = set()
        trips = trips_on_target(trip_set, STOP_3144, STOP_4517)
        assert trips == ans

    def test_trips_not_on_target(self):
        """Trips departure time later as arrival"""
        ans = set()
        trip_set = {trip_3_10000004}
        trips = trips_on_target(trip_set, STOP_3144, STOP_4517)
        assert trips == ans

    def test_one_wrong_trip(self):
        """Filters one trip which does not fulfill 'departure before arrival'"""
        ans = {trip_3_10000002, trip_3_10000003}
        trips_set = {trip_3_10000002, trip_3_10000003, trip_3_10000004}
        trips = trips_on_target(trips_set, STOP_3144, STOP_4517)
        assert trips == ans


class TestTripByArrivalTime:
    """Sort the trips with key 'arrival time' at given stop (earlier better)"""

    def test_two_trips(self):
        """Two trips"""
        ans = [trip_3_10000002, trip_3_10000003]
        trip_set = {trip_3_10000003, trip_3_10000002}
        trips = trip_by_arrival_time(trip_set, STOP_3144)
        assert trips == ans

    def test_no_trips(self):
        """No trips"""
        ans = []
        trip_set = set()
        trips = trip_by_arrival_time(trip_set, STOP_3144)
        assert trips == ans


class TestFindTrips:
    """Finding correct trips between two stops
    Conditions:
     a) Trip must cross both stops
     b) Start stop must be before target stop
     == Start stops must be before target stop in bus/tram timetable (direction condition)
    """

    @patch('backend.src.controller.find_trips.query_trip_ids')
    @patch('backend.src.controller.find_trips.TripSQLDirector.construct')
    def test_happy_path(self, mock_construct, mock_query_id_patch):
        """The same trip in correct direction"""
        mock_trip = TripStandardDirector.construct('3_10000004', STOP_TIMETABLE_TRIP_3_10000004)
        ans = {mock_trip}
        mock_query_id_patch.side_effect = [{'3_10000004'}, {'3_10000004'}]
        mock_construct.side_effect = iter((mock_trip,))
        result = find_trips(STOP_4517, STOP_3144)
        assert result == ans

    @patch('backend.src.controller.find_trips.query_trip_ids')
    @patch('backend.src.controller.find_trips.TripSQLDirector.construct')
    def test_no_trips(self, mock_construct, mock_query_id_patch):
        """No common trips"""
        mock_trip = TripStandardDirector.construct('3_10000004', STOP_TIMETABLE_TRIP_3_10000004)
        ans = {}
        mock_query_id_patch.side_effect = [{}, {}]
        mock_construct.side_effect = iter((mock_trip,))
        result = find_trips(STOP_4517, STOP_3144)
        assert {} == ans

    @patch('backend.src.controller.find_trips.query_trip_ids')
    @patch('backend.src.controller.find_trips.TripSQLDirector.construct')
    def test_no_trips(self, mock_construct, mock_query_id_patch):
        """No trips"""
        mock_trip = TripStandardDirector.construct('3_10000004', STOP_TIMETABLE_TRIP_3_10000004)
        ans = {}
        mock_query_id_patch.side_effect = [{'3_10000001'}, {'3_10000004'}]
        mock_construct.side_effect = iter((mock_trip,))
        result = find_trips(STOP_4517, STOP_3144)
        assert {} == ans

    @patch('backend.src.controller.find_trips.query_trip_ids')
    @patch('backend.src.controller.find_trips.TripSQLDirector.construct')
    def test_no_trips_target(self, mock_construct, mock_query_id_patch):
        """Trip not on target (wrong direction)"""
        mock_trip = TripStandardDirector.construct('3_10000003', STOP_TIMETABLE_TRIP_3_10000003)
        ans = set()
        mock_query_id_patch.side_effect = [{'3_10000003'}, {'3_10000003'}]
        mock_construct.side_effect = iter((mock_trip,))
        result = find_trips(STOP_4517, STOP_3144)
        assert result == ans
