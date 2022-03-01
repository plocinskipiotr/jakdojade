import datetime
from typing import Iterator

from backend.src.controller.trip import Trip
from backend.src.model.db_queries import query_geoloc, query_trips
from backend.src.controller.geolocation import GeoPoint


class Stop():

    def __init__(self, city: str, stop_id: int, curr_time=datetime.datetime.now().strftime('%H:%M:%S')):
        self.city: str = city
        self.stop_id: int = stop_id
        self.curr_time: str = curr_time
        self.geopoint: GeoPoint = self.to_geopoint(query_geoloc(self.city, self.stop_id))
        self.trips: set[Trip] = self.to_set(query_trips(self.city, self.stop_id, self.curr_time))

    def to_set(self, iterator: Iterator[tuple]):
        return {Trip(self.city, el[0]) for el in iterator}

    def to_geopoint(self, iterator: Iterator[tuple]):
        single_point = list(iterator)[0]
        d = {'latitude': single_point[0],
             'longitude': single_point[1]}
        return GeoPoint(d)

    def __eq__(self, other):
        return self.stop_id == other.stops_departure

    def __ne__(self, other):
        return self.stop_id != other.stops_departure
