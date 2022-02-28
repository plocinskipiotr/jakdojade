import datetime

from sqlalchemy import select

from backend.src.db_table_to_class import TableToClass
from backend.src.endpoints_queries import session
from backend.src.trip import Trip
from backend.src.geolocation import GeoPoint


class Stop:

    def __init__(self, city, stop_id, curr_time=datetime.datetime.now().strftime('%H:%M:%S')):
        self.city = city
        self.stop_id = stop_id
        self.geopoint = self._get_geopoint()
        self.curr_time = curr_time
        self.trips = self._get_trips()

    def _get_trips(self):
        tab_obj = TableToClass.parse(self.city + '_stop_times')
        trip_res = session.execute(select(tab_obj.trip_id)
                                   .where(tab_obj.stop_id == self.stop_id,
                                          tab_obj.departure_time > self.curr_time)
                                   .order_by(tab_obj.trip_id))
        trip_ids = list(trip_res)
        trip_lst = [Trip(self.city, trip_id[0]) for trip_id in trip_ids]
        return set(trip_lst)

    def _get_geopoint(self):
        tab_obj = TableToClass.parse(self.city + '_stops')
        geo_loc = session.execute(select(tab_obj.stop_lat, tab_obj.stop_lon)
                                  .where(tab_obj.stop_id == self.stop_id))
        geo_loc = list(geo_loc)
        lat, lon = geo_loc[0][0], geo_loc[0][1]
        return GeoPoint(lat, lon)

    def next_departure(self, other: 'Stop'):
        #common_trips = self.trips & other.trips
        common_trips_lst = []
        for item1 in self.trips:
            for item2 in other.trips:
                if item1.trip_id == item2.trip_id:
                    common_trips_lst.append(item1)

        #common_trips = self.trips.intersection(other.trips)
        #common_trips_lst = list(common_trips)
        common_trips_lst.sort(key=lambda x: x.start_time)
        for trip in common_trips_lst:
            if trip.ids_dep_time[self.stop_id] < trip.ids_dep_time[other.stop_id]:
                return trip


    def __eq__(self, other):
        return self.stop_id == other.stop_id

    def __ne__(self, other):
        return self.stop_id != other.stop_id
