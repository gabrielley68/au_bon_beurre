import json
import os
import random
import socket

unit_number = os.environ['unit_number']

automats = {
    1: 0X0000BA20,
    2: 0X0000BA21,
    3: 0X0000BA22,
    4: 0X0000BA23,
    5: 0X0000BA24,
    6: 0X0000BA25,
    7: 0X0000BA26,
    8: 0X0000BA27,
    9: 0X0000BA28,
    10: 0X0000BA29
}


def random_data(unit_number, automat_number, automat_type):
    tank_temperature = round(random.uniform(2.4, 4.0), 1)
    outside_temperature = round(random.uniform(8.0, 14.0), 1)
    milk_weight_in_tank = random.randint(3512, 4607)
    ph_measurement = round(random.uniform(6.8, 7.2), 1)
    k_plus_measurement = random.randint(35, 47)
    nacl_concentration = round(random.uniform(1.0, 1.7), 1)
    salmonella_level = random.randint(17, 37)
    e_coli_level = random.randint(35, 49)
    listeria_level = random.randint(28, 54)

    data_set = {
        "unit_no": unit_number,
        "automate_no": automat_number,
        "type_automate": automat_type,
        "tank_temperature": tank_temperature,
        "ext_temperature": outside_temperature,
        "milk_weight_tank": milk_weight_in_tank,
        "ph": ph_measurement,
        "k_plus": k_plus_measurement,
        "nacl_concentration": nacl_concentration,
        "salmonella_bacteria_level": salmonella_level,
        "e_coli_bacteria_level": e_coli_level,
        "listeria_bacteria_level": listeria_level
    }

    # json format
    json_dump = json.dumps(data_set)
    # dict format
    json_object = json.loads(json_dump)

    return json_object


random_jsons = []

for automat_number, automat_type in automats.items():
    random_jsons.append(random_data(unit_number, automat_number, automat_type))

host = "mds_ias_collecteur"
port = 5001

s = socket.socket()
s.connect((host, port))
s.send(json.dumps(random_jsons).encode("utf-8"))
