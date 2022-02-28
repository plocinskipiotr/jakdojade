import datetime
from collections import namedtuple

from flask import jsonify
from sqlalchemy import select

from backend.src.endpoints_func import find_closest_stops
from backend.src.user import User
from backend.src.constants import DB_CONF, POSTGRES
from backend.src.db_model import Cities, Stops
from backend.src.db_service import DBService
from backend.src.db_table_to_class import TableToClass

db = DBService(DB_CONF, POSTGRES)
session_maker = db.get_sessionmaker()
session = session_maker()


def get_cities():
    result = session.query(Cities).all()
    result = [item.serialize() for item in result]
    result = jsonify(result)
    return result


def get_routes(city: str):
    routes = session.query(TableToClass.parse(city + '_routes')).all()
    return routes


def get_stops(city: str, user: User, stop_limit=5):
    stop_list = session.query(TableToClass.parse(city + '_stops')).all()
    result = find_closest_stops(user, stop_list, stop_limit)
    return result


# Trips = namedtuple('Trip', ['id', 'departure_time', 'stop_id'])


def get_trips(city: str, stop: Stops):
    tab_obj = TableToClass.parse(city + '_stop_times')
    trip_res = session.execute(select(tab_obj.trip_id, tab_obj.departure_time)
                               .where(tab_obj.stop_id == stop.stop_id)
                               .order_by(tab_obj.trip_id))
    trip_lst = list(trip_res)
    return trip_lst

    # trip_res = session.query(tab_obj).filter(tab_obj.stop_id == stop_id,
    #                                         tab_obj.departure_time >= time)
    # trip_list = [Trips(item.trip_id, item.departure_time, item.stop_id) for item in trip_res]
    # trip_list = sorted(list(trip_list), key=lambda x: x.departure_time)

    # for item in trip_list:


def stops_in_trip(city: str, trip_id: str):
    tab_obj = TableToClass.parse(city + '_stop_times')
    stops = session.execute(select(tab_obj.stop_id).where(tab_obj.trip_id == trip_id) \
                            .order_by(tab_obj.stop_id))
    return stops
