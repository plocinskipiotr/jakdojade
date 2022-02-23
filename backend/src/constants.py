WROCLAW_ROUTES_TXT = '../data/routes/wroclaw.txt'
POSTGRES = 'postgres'
DB_CONF = '../db/db_conf.json'
ROUTES_DIR = '../data/routes'
CITIES_FILE = '../data/cities.txt'

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