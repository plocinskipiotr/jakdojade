import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent.parent
POSTGRES = 'postgres'
DB_CONF = os.path.join(ROOT_DIR, 'backend/db/db_conf.json')
