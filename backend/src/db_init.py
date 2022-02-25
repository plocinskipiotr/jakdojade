from backend.src.data_transformations import city_trans, route_trans, stop_times_trans, \
    stop_trans, trips_trans
from backend.src.etl_process import SimpleETL
from backend.src.constants import DB_CONF, CITIES_FILE, ROUTES_DIR, STOPS_DIR, STOP_TIMES_DIR, TRIPS_DIR, POSTGRES
from backend.src.db_service import DBService


def db_init():
    db = DBService(DB_CONF, POSTGRES)
    db.build_schema()
    SimpleETL.file(CITIES_FILE, city_trans(), db)
    SimpleETL.directory(ROUTES_DIR, route_trans(), db)
    SimpleETL.directory(STOP_TIMES_DIR, stop_times_trans(), db)
    SimpleETL.directory(STOPS_DIR, stop_trans(), db)
    SimpleETL.directory(TRIPS_DIR, trips_trans(), db)
