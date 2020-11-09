# Module Import
import mariadb
import sys
import os
from pathlib import Path

# Pull defaults from OS environment if they exist
user = os.environ.get('MARIADB_USER', 'connpy_test')
# Prefer secret for mariadb_pass if a secret exists
if Path('/run/secrets/mariadb_pass').is_file():
   with open("/run/secrets/mariadb_pass", "r") as password_file:
      password = password_file.read()
else:
   password = os.environ.get('MARIADB_PASS', 'passwd')
host = os.environ.get('MARIADB_HOST', 'localhost')
port = int(os.environ.get('MARIADB_PORT', 3306))

# Instantiate Connection
try:
   conn = mariadb.connect(
      user=user,
      password=password,
      host=host,
      port=port)
except mariadb.Error as e:
   print(f"Error connecting to MariaDB Platform: {e}")
   sys.exit(1)