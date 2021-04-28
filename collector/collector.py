import json
import mariadb
import sys
import socket

from automate import Automate

DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_DATABASE = "automate"

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step
SOCKET_HOST = "127.0.0.1"
SOCKET_PORT = 5001

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
cur.execute("CREATE DATABASE {}".format(DB_DATABASE))

query = """CREATE TABLE IF NOT EXISTS {} ( 
                unit_no int(10),
                automate_no int(10),
                type_automate int(10),
                tank_temperature FLOAT(8,2),
                ext_temperature FLOAT(8,2),
                milk_weight_tank int(10),
                final_weight int(10),
                ph FLOAT(8,2),
                k_plus int(10),
                nacl_concentration FLOAT(8,2),
                salmonella_bacteria_level int(10),
                e_coli_bacteria_level int(10),
                listeria_bacteria_level int(10) ); """.format(DB_DATABASE)

# To execute the SQL query
cur.execute(query)

s = socket.socket()
s.bind((SOCKET_HOST, SOCKET_PORT))
s.listen()
while True:
    client_socket, address = s.accept()
    json_data = json.loads(s.recv(BUFFER_SIZE).decode("utf-8"))

    # Get Cursor
    cur = conn.cursor()

    # Insert in db all data.
    for automate in Automate.json_to_class(json_data):
        cur.execute("INSERT INTO automate (unit_no,automate_no,type_automate,tank_temperature,ext_temperature,"
                    "milk_weight_tank,final_weight,ph,k_plus,nacl_concentration,salmonella_bacteria_level,"
                    "e_coli_bacteria_level,listeria_bacteria_level) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                    (automate.get_unit_no, automate.get_automate_no, automate.get_type_automate,
                     automate.get_tank_temperature, automate.get_ext_temperature, automate.get_milk_weight_tank,
                     automate.get_final_weight, automate.get_ph, automate.get_k_plus, automate.get_nacl_concentration,
                     automate.get_salmonella_bacteria_level, automate.get_e_coli_bacteria_level,
                     automate.get_listeria_bacteria_level))

    conn.close()
