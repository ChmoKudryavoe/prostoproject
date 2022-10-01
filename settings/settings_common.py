"""Common settings are defined here. Only upper case variables are exported."""

import os


APP_ROOT = os.path.dirname(os.path.dirname(__file__))
DB_NAME = 'main.db'
DB2_NAME = 'users.db'
DATABASE2 = os.path.join(APP_ROOT, DB2_NAME)
DATABASE = os.path.join(APP_ROOT, DB_NAME)
