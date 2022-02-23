from constants import POL_TO_ENG, ROUTES_DIR, CITIES_FILE
from db_service import DBService
from city_container import CityContainer
from etl_process import SimpleETL


def route_transformation() -> callable:
    return lambda x: {'route_id': x[0], 'route_short_name': x[2], 'route_desc': x[4]}


def city_transformation() -> callable:
    return lambda x: {'city_id': x[0], 'city_name': x[1].translate(POL_TO_ENG).lower()}


def create_db_schema(db: DBService):
    db.build_schema()


def populate_db_schema(db: DBService, cities_f=CITIES_FILE, routes_f=ROUTES_DIR):
    SimpleETL.file(cities_f, city_transformation(), db)
    SimpleETL.directory(routes_f, route_transformation(), db)
