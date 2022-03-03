from backend.src.controller.trip import Trip
from backend.src.controller.trip_builder import TripSQLDirector

STOP_TIMETABLES = {1002: {'arrival': '07:11:00', 'departure': '07:11:00'},
                   2011: {'arrival': '07:13:00', 'departure': '07:13:00'},
                   337: {'arrival': '07:14:00', 'departure': '07:14:00'},
                   941: {'arrival': '07:17:00', 'departure': '07:17:00'},
                   4397: {'arrival': '07:21:00', 'departure': '07:21:00'},
                   4390: {'arrival': '07:22:00', 'departure': '07:22:00'},
                   4398: {'arrival': '07:23:00', 'departure': '07:23:00'},
                   4389: {'arrival': '07:24:00', 'departure': '07:24:00'},
                   4399: {'arrival': '07:26:00', 'departure': '07:26:00'},
                   4394: {'arrival': '07:27:00', 'departure': '07:27:00'},
                   4402: {'arrival': '07:28:00', 'departure': '07:28:00'},
                   4410: {'arrival': '07:29:00', 'departure': '07:29:00'},
                   4411: {'arrival': '07:30:00', 'departure': '07:30:00'},
                   4393: {'arrival': '07:32:00', 'departure': '07:32:00'},
                   4400: {'arrival': '07:34:00', 'departure': '07:34:00'},
                   4404: {'arrival': '07:35:00', 'departure': '07:35:00'},
                   2665: {'arrival': '07:36:00', 'departure': '07:36:00'},
                   2264: {'arrival': '07:37:00', 'departure': '07:37:00'},
                   356: {'arrival': '07:38:00', 'departure': '07:38:00'},
                   348: {'arrival': '07:39:00', 'departure': '07:39:00'},
                   1114: {'arrival': '07:40:00', 'departure': '07:40:00'},
                   2037: {'arrival': '07:42:00', 'departure': '07:42:00'},
                   357: {'arrival': '07:43:00', 'departure': '07:43:00'},
                   1215: {'arrival': '07:44:00', 'departure': '07:44:00'},
                   3876: {'arrival': '07:45:00', 'departure': '07:45:00'},
                   3760: {'arrival': '07:46:00', 'departure': '07:46:00'},
                   2288: {'arrival': '07:48:00', 'departure': '07:48:00'},
                   481: {'arrival': '07:49:00', 'departure': '07:49:00'},
                   2374: {'arrival': '07:50:00', 'departure': '07:50:00'},
                   509: {'arrival': '07:53:00', 'departure': '07:53:00'},
                   3518: {'arrival': '07:54:00', 'departure': '07:54:00'}}


class TestTrip:

    def test_trip(self):
        t = TripSQLDirector.construct('3_10090600')
        assert isinstance(t, Trip)
        assert t.id == '3_10090600'
        assert t.stop_timetables == STOP_TIMETABLES

    def test_trip_fail(self):
        t = TripSQLDirector.construct('3_32')
        assert isinstance(t, Trip)
        assert t.id == '3_32'
        assert t.stop_timetables == {}
