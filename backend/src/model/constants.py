import logging
import os
from pathlib import Path
from settings import ROOT_DIR

# Database configuration file
DB_CONF = os.path.join(ROOT_DIR, 'backend/db/db_conf.json')
# Database type
POSTGRES = 'postgres'
# City used in queries
CITY = 'wroclaw'

logging.warning('db transaction only for ' + CITY + ' are enabled. more info ' + str(Path(__file__)))
