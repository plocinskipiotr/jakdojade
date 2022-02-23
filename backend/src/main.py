from city_container import CityContainer
from create_populate_db import create_db_schema, populate_db_schema
from constants import DB_CONF
from db_service import DBService

if __name__ == "__main__":
    db = DBService(DB_CONF, 'postgres')
    city_container = CityContainer()
    create_db_schema(db)
    populate_db_schema(db)
