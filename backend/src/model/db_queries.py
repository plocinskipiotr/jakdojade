from sqlalchemy import select

from backend.src.model.constants import DB_CONF, POSTGRES
from backend.src.model.db_base import Cities
from backend.src.model.db_service import DBService
from backend.src.model.db_table_to_class import TableToClass

db = DBService(DB_CONF, POSTGRES)
session_maker = db.get_sessionmaker()
session = session_maker()


def query_cities():
    result = session.query(Cities).all()
    return result


def query_routes(city: str):
    result = session.query(TableToClass.parse(city + '_routes')).all()
    return result


def query_stops(city: str):
    result = session.query(TableToClass.parse(city + '_stops')).all()
    return result


def query_stop_time_tables(city: str, trip_id: str):
    tab_obj = TableToClass.parse(city + '_stop_times')
    result = session.execute(select(tab_obj.stop_id, tab_obj.arrival_time, tab_obj.departure_time)
                             .where(tab_obj.trip_id == trip_id))

    return result


def query_trip_ids(city: str, stop_id: int):
    tab_obj = TableToClass.parse(city + '_stop_times')
    result = session.execute(select(tab_obj.trip_id)
                             .where(tab_obj.stop_id == stop_id)
                             .order_by(tab_obj.trip_id))
    return result


def query_geoloc(city: str, stop_id: int):
    tab_obj = TableToClass.parse(city + '_stops')
    result = session.execute(select(tab_obj.stop_lat, tab_obj.stop_lon)
                             .where(tab_obj.stop_id == stop_id))
    return result
