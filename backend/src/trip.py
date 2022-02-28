from sqlalchemy import select

from backend.src.db_table_to_class import TableToClass
from backend.src.endpoints_queries import session


class Trip:

    def __init__(self, city, trip_id):
        self.city = city
        self.trip_id = trip_id
        self.ids_dep_time = self._get_stop_time()
        self.start_time = min(self.ids_dep_time.values())

    def _get_stop_time(self):
        tab_obj = TableToClass.parse(self.city + '_stop_times')
        stop_time = session.execute(select(tab_obj.stop_id, tab_obj.departure_time)
                                    .where(tab_obj.trip_id == self.trip_id) \
                                    .order_by(tab_obj.departure_time))

        t = tuple(stop_time)
        d = dict(t)
        return d

    def _get_min_stop_time(self):
        return min(self.ids_dep_time.values())

    def __eq__(self, other):
        return self.trip_id == other.trip_id

    def __ne__(self, other):
        return self.trip_id != other.trip_id

    def __hash__(self):
        return id(self)
