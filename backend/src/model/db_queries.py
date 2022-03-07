from typing import Iterator

from sqlalchemy import select

from settings import DB_CONF, POSTGRES, CITY
from backend.src.model.db_model import Cities, Routes, Stops
from backend.src.model.db_service import DBService
from backend.src.model.db_table_to_class import TableToClass

db = DBService(DB_CONF, POSTGRES)
session_maker = db.get_sessionmaker()
session = session_maker()


def query_cities() -> Iterator[Cities]:
    """query all rows from table Cities"""
    result = session.query(Cities).all()
    return result


def query_routes(city: str = CITY) -> Iterator[Routes]:
    """query all transport routes for given city"""
    result = session.query(TableToClass.parse(city + '_routes')).all()
    return result


def query_stops(city: str = CITY) -> Iterator[Stops]:
    """query all stops for given city"""
    result = session.query(TableToClass.parse(city + '_stops')).all()
    return result


def query_stop_name(stop_id: int, city: str = CITY) -> Iterator[tuple[str]]:
    """query stop name for given stop id"""
    tab_obj = TableToClass.parse(city + '_stops')
    result = session.execute(select(tab_obj.stop_name).where(tab_obj.stop_id == stop_id))
    return result


def query_gps_coordinates(stop_id: int, city: str = CITY) -> Iterator[tuple[float, float]]:
    """query gps coordinates for given stop id / city"""
    tab_obj = TableToClass.parse(city + '_stops')
    result = session.execute(select(tab_obj.stop_lat, tab_obj.stop_lon)
                             .where(tab_obj.stop_id == stop_id))
    return result


def query_stop_time_tables(trip_id: str, city: str = CITY) -> Iterator[tuple[int, str, str, str]]:
    """query stop timetable for given trip id (stop id,stop name, arrival time, departure time)"""
    stop_times = TableToClass.parse(city + '_stop_times')
    stops = TableToClass.parse(city + '_stops')
    result = session.execute(
        select(stop_times.stop_id, stops.stop_name, stop_times.arrival_time, stop_times.departure_time).where(
            stop_times.trip_id == trip_id, stop_times.stop_id == stops.stop_id))

    return result


def query_trip_ids(stop_id: int, city: str = CITY) -> Iterator[tuple[str]]:
    """query trip ids which visit given stop"""
    tab_obj = TableToClass.parse(city + '_stop_times')
    result = session.execute(select(tab_obj.trip_id)
                             .where(tab_obj.stop_id == stop_id)
                             .order_by(tab_obj.trip_id))
    return result
