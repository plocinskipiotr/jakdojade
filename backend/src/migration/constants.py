import os
from pathlib import Path

from backend.settings import ROOT_DIR

ROUTES_DIR = os.path.join(ROOT_DIR, Path('data/routes'))
STOP_TIMES_DIR = os.path.join(ROOT_DIR, 'data/stop_times')
STOPS_DIR = os.path.join(ROOT_DIR, 'data/stops')
TRIPS_DIR = os.path.join(ROOT_DIR, 'data/trips')
CITIES_FILE = os.path.join(ROOT_DIR, 'data/cities.txt')

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
