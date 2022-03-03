"""This file contains db_init which is used to drop/create database schema
and for loading the data"""

import os
from pathlib import Path

from backend.src.migration.data_transformations import city_trans, route_trans, stop_times_trans, \
    stop_trans, trips_trans
from backend.src.migration.etl_process import SimpleETL
from backend.src.model.db_queries import db
from settings import ROOT_DIR

ROUTES_DIR = os.path.join(ROOT_DIR, Path('backend/data/routes'))
STOP_TIMES_DIR = os.path.join(ROOT_DIR, 'backend/data/stop_times')
STOPS_DIR = os.path.join(ROOT_DIR, 'backend/data/stops')
TRIPS_DIR = os.path.join(ROOT_DIR, 'backend/data/trips')
CITIES_FILE = os.path.join(ROOT_DIR, 'backend/data/cities.txt')


def db_init():
    db.build_schema()
    SimpleETL.file(CITIES_FILE, city_trans(), db)
    SimpleETL.directory(ROUTES_DIR, route_trans(), db)
    SimpleETL.directory(STOP_TIMES_DIR, stop_times_trans(), db)
    SimpleETL.directory(STOPS_DIR, stop_trans(), db)
    SimpleETL.directory(TRIPS_DIR, trips_trans(), db)
