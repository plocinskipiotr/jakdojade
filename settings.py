import os
import logging
import sys

ROOT_DIR = str(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)
# Database configuration file
DB_CONF = os.path.join(ROOT_DIR, 'backend/db/db_conf.json')
# Database type
POSTGRES = 'postgres'
# City used in queries
CITY = 'wroclaw'

logging.warning('db transaction only for ' + CITY + ' are enabled. more info ' + str(os.path.abspath(__file__)))
