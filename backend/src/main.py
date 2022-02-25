from etl_process import SimpleETL
from constants import DB_CONF, CITIES_FILE, POL_TO_ENG, ROUTES_DIR, STOPS_DIR, STOP_TIMES_DIR, TRIPS_DIR, POSTGRES
from db_service import DBService


def route_transformation() -> callable:
    return lambda x: {'route_id': x[0], 'route_short_name': x[2], 'route_desc': x[4]}


def city_transformation() -> callable:
    return lambda x: {'city_id': x[0], 'city_name': x[1].translate(POL_TO_ENG).lower()}


def stop_times_transformation() -> callable:
    return lambda x: {'trip_id': x[0], 'arrival_time': x[1], 'departure_time': x[2], 'stop_id': x[3]}


def stop_transformation() -> callable:
    return lambda x: {'stop_id': x[0], 'stop_name': x[2], 'stop_lat': x[3], 'stop_lon': x[4]}


def trips_transformation() -> callable:
    return lambda x: {'route_id': x[0], 'trip_id': x[2], 'trip_headsign': x[3]}


if __name__ == "__main__":
    db = DBService(DB_CONF, POSTGRES)
    db.build_schema()
    SimpleETL.file(CITIES_FILE, city_transformation(), db)
    SimpleETL.directory(ROUTES_DIR, route_transformation(), db)
    SimpleETL.directory(STOP_TIMES_DIR, stop_times_transformation(), db)
    SimpleETL.directory(STOPS_DIR, stop_transformation(), db)
    SimpleETL.directory(TRIPS_DIR, trips_transformation(), db)
