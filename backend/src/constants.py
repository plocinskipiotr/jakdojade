import os
from pathlib import Path

POSTGRES = 'postgres'
ROOT_DIR = Path(__file__).parent.parent.parent

DB_CONF = os.path.join(ROOT_DIR, 'backend/db/db_conf.json')
ROUTES_DIR = os.path.join(ROOT_DIR, 'backend/data/routes')
STOP_TIMES_DIR = os.path.join(ROOT_DIR, 'backend/data/stop_times')
STOPS_DIR = os.path.join(ROOT_DIR, 'backend/data/stops')
TRIPS_DIR = os.path.join(ROOT_DIR, 'backend/data/trips')
CITIES_FILE = os.path.join(ROOT_DIR, 'backend/data/cities.txt')

POL_TO_ENG = {ord('ł'): ord('l'),
              ord('ą'): ord('a'),
              ord('ć'): ord('c'),
              ord('ę'): ord('e'),
              ord('ń'): ord('n'),
              ord('ó'): ord('o'),
              ord('ź'): ord('z'),
              ord('ż'): ord('z'),
              ord('ś'): ord('s')
              }
