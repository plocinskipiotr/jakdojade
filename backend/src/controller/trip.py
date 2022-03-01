from typing import Iterator
from backend.src.model.db_queries import query_stop_deps, query_stop_arrivals


class Trip:

    def __init__(self, city, trip_id):
        self.city: str = city
        self.trip_id: int = trip_id
        self.stops_departure: dict = self.to_dict(query_stop_deps(self.city, self.trip_id))
        self.stops_arrival: dict = self.to_dict(query_stop_arrivals(self.city, self.trip_id))
        self.stops: set[int] = set(self.stops_departure.keys())

    def to_dict(self, lst_iterator: Iterator[tuple]):
        d = {}
        for item in lst_iterator:
            key, val = item[0], item[1]
            d.update({key: val})
        return d

    def __eq__(self, other):
        return self.trip_id == other.trip_id

    def __ne__(self, other):
        return self.trip_id != other.trip_id

    def __hash__(self):
        return int(self.trip_id)
