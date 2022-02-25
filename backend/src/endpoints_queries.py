from flask import jsonify
from backend.src.endpoints_func import find_closest_stops
from backend.src.user import User
from backend.src.constants import DB_CONF, POSTGRES
from backend.src.db_model import Cities
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
    result = session.query(TableToClass.parse(city + '_routes')).all()
    result = [item.serialize() for item in result]
    result = jsonify(result)
    return result


def get_stops(city: str, user: User):
    stop_list = session.query(TableToClass.parse(city + '_stops')).all()
    result = find_closest_stops(user, stop_list)
    result = [item.serialize() for item in result]
    result = jsonify(result)
    return result
