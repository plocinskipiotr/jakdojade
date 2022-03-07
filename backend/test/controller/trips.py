from backend.src.controller.trip_builder import TripStandardDirector

STOP_TIMETABLE_TRIP_3_10000000 = \
    {3144: {'name': 'KOSZAROWA (Szpital)', 'arrival': '20:41:00', 'departure': '20:41:00'},
     2828: {'name': 'Psie Pole', 'arrival': '20:50:00', 'departure': '20:50:00'},
     4588: {'name': 'Bierutowska 75', 'arrival': '20:52:00', 'departure': '20:52:00'}
     }

STOP_TIMETABLE_TRIP_3_10000001 = \
    {4517: {'name': 'Ogród Botaniczny', 'arrival': '20:41:00', 'departure': '20:41:00'},
     3222: {'name': 'Małopolska', 'arrival': '20:43:00', 'departure': '20:43:00'},
     1229: {'name': 'Armii Krajowej', 'arrival': '20:52:00', 'departure': '20:52:00'}
     }

STOP_TIMETABLE_TRIP_3_10000002 = \
    {3144: {'name': 'KOSZAROWA (Szpital)', 'arrival': '20:11:00', 'departure': '20:11:00'},
     615: {'name': 'Wyszyńskiego', 'arrival': '20:20:00', 'departure': '20:20:00'},
     4517: {'name': 'Ogród Botaniczny', 'arrival': '20:22:00', 'departure': '20:22:00'}
     }

STOP_TIMETABLE_TRIP_3_10000003 = \
    {3144: {'name': 'KOSZAROWA (Szpital)', 'arrival': '20:50:00', 'departure': '20:50:00'},
     615: {'name': 'Wyszyńskiego', 'arrival': '20:54:00', 'departure': '20:54:00'},
     4517: {'name': 'Ogród Botaniczny', 'arrival': '20:58:00', 'departure': '20:58:00'}
     }

STOP_TIMETABLE_TRIP_3_10000004 = \
    {4517: {'name': 'Ogród Botaniczny', 'arrival': '20:50:00', 'departure': '20:50:00'},
     615: {'name': 'Wyszyńskiego', 'arrival': '20:54:00', 'departure': '20:54:00'},
     3144: {'name': 'KOSZAROWA (Szpital)', 'arrival': '20:58:00', 'departure': '20:58:00'}
     }

trip_3_10000000 = TripStandardDirector.construct('3_10000000', STOP_TIMETABLE_TRIP_3_10000000)
trip_3_10000001 = TripStandardDirector.construct('3_10000001', STOP_TIMETABLE_TRIP_3_10000001)

trip_3_10000002 = TripStandardDirector.construct('3_10000002', STOP_TIMETABLE_TRIP_3_10000002)
trip_3_10000003 = TripStandardDirector.construct('3_10000003', STOP_TIMETABLE_TRIP_3_10000003)
trip_3_10000004 = TripStandardDirector.construct('3_10000004', STOP_TIMETABLE_TRIP_3_10000004)
