import logging
import os
from pathlib import Path
from backend.settings import ROOT_DIR

# Data base configuration file
DB_CONF = os.path.join(ROOT_DIR, 'db/db_conf.json')
# Data base type
POSTGRES = 'postgres'
# City used in queries
CITY = 'wroclaw'

logging.warning('db transaction only for ' + CITY + ' are enabled\n more info ' + str(Path(__file__)))
