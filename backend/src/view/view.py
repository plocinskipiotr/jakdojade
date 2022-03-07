from collections import namedtuple

from backend.src.controller.trip import Trip

row = namedtuple('row', ['arrival', 'departure', 'name'])


def trip_by_departure(trip: Trip):
    lst = []
    for k, v in trip.stop_timetable.items():
        item = (k, row(arrival=v['arrival'], departure=v['departure'], name=v['name']))
        lst.append(item)
    lst.sort(key=lambda x: x[1].departure)
    lst = [(item[0], {'name': item[1].name, 'arrival': item[1].arrival, 'departure': item[1].departure}) for item in
           lst]
    trip.stop_timetable = lst
    return trip
