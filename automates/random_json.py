import json
import os
import random

unit_number = os.environ['unit_number']
automat_number = os.environ['automat_number']
automat_type = os.environ['automat_type']


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
        "unit_number": unit_number,
        "automat_number": automat_number,
        "automat_type": automat_type,
        "tank_temperature": tank_temperature,
        "outside_temperature": outside_temperature,
        "milk_weight_in_tank": milk_weight_in_tank,
        "ph_measurement": ph_measurement,
        "k_plus_measurement": k_plus_measurement,
        "nacl_concentration": nacl_concentration,
        "salmonella_level": salmonella_level,
        "e_coli_level": e_coli_level,
        "listeria_level": listeria_level
    }

    # json format
    json_dump = json.dumps(data_set)
    # dict format
    json_object = json.loads(json_dump)

    return json_object


random_data(unit_number, automat_number, automat_type)
