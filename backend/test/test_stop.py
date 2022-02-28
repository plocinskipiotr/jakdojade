from sqlalchemy import select

from backend.src.db_table_to_class import TableToClass
from backend.src.endpoints_queries import session
from backend.src.stop import Stop


class TestStop:

    def test_stop(self):
        s = Stop('wroclaw', 357)

    def test_create_stop_map(self):
        tab_obj = TableToClass.parse('wroclaw' + '_stops')
        stop_ids = session.execute(select(tab_obj.stop_id).where(tab_obj.stop_id < 10))
        stop_ids = [stop_id[0] for stop_id in stop_ids]
        stops = [Stop('wroclaw', stop_id) for stop_id in stop_ids]
