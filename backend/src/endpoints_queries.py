from flask import jsonify
from backend.src.constants import DB_CONF, POSTGRES
from backend.src.db_model import Cities
from backend.src.db_service import DBService
from backend.src.db_model import TableToClassParser

db = DBService(DB_CONF, POSTGRES)
session_maker = db.get_sessionmaker()
session = session_maker()


def get_cities():
    result = session.query(Cities).all()
    result = [item.serialize() for item in result]
    result = jsonify(result)
    return result


def get_routes(city: str):
    result = session.query(TableToClassParser.parse(city)).all()
    result = [item.serialize() for item in result]
    result = jsonify(result)
    return result
