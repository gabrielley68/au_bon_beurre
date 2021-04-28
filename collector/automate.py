class Automate:
    def __init__(self,
                 unit_no: int,
                 automate_no: int,
                 type_automate: int,
                 tank_temperature: float,
                 ext_temperature: float,
                 milk_weight_tank: int,
                 final_weight: int,
                 ph: float,
                 k_plus: int,
                 nacl_concentration: float,
                 salmonella_bacteria_level: int,
                 e_coli_bacteria_level: int,
                 listeria_bacteria_level: int):
        self.unit_no = unit_no
        self.automate_no = automate_no
        self.type_automate = type_automate
        self.tank_temperature = tank_temperature
        self.ext_temperature = ext_temperature
        self.milk_weight_tank = milk_weight_tank
        self.final_weight = final_weight
        self.ph = ph
        self.k_plus = k_plus
        self.nacl_concentration = nacl_concentration
        self.salmonella_bacteria_level = salmonella_bacteria_level
        self.e_coli_bacteria_level = e_coli_bacteria_level
        self.listeria_bacteria_level = listeria_bacteria_level

    def get_unit_no(self):
        return self.unit_no

    def set_automate_no(self, automate_no):
        self.automate_no = automate_no

    def get_automate_no(self):
        return self.automate_no

    def set_type_automate(self, type_automate):
        self.type_automate = type_automate

    def get_type_automate(self):
        return self.type_automate

    def set_tank_temperature(self, tank_temperature):
        self.tank_temperature = tank_temperature

    def get_tank_temperature(self):
        return self.tank_temperature

    def set_ext_temperature(self, ext_temperature):
        self.ext_temperature = ext_temperature

    def get_ext_temperature(self):
        return self.ext_temperature

    def set_milk_weight_tank(self, milk_weight_tank):
        self.milk_weight_tank = milk_weight_tank

    def get_milk_weight_tank(self):
        return self.milk_weight_tank

    def set_final_weight(self, final_weight):
        self.final_weight = final_weight

    def get_final_weight(self):
        return self.final_weight

    def set_ph(self, ph):
        self.ph = ph

    def get_ph(self):
        return self.ph

    def set_k_plus(self, k_plus):
        self.k_plus = k_plus

    def get_k_plus(self):
        return self.k_plus

    def set_nacl_concentration(self, nacl_concentration):
        self.nacl_concentration = nacl_concentration

    def get_nacl_concentration(self):
        return self.nacl_concentration

    def set_salmonella_bacteria_level(self, salmonella_bacteria_level):
        self.salmonella_bacteria_level = salmonella_bacteria_level

    def get_salmonella_bacteria_level(self):
        return self.salmonella_bacteria_level

    def set_e_coli_bacteria_level(self, e_coli_bacteria_level):
        self.e_coli_bacteria_level = e_coli_bacteria_level

    def get_e_coli_bacteria_level(self):
        return self.e_coli_bacteria_level

    def set_listeria_bacteria_level(self, listeria_bacteria_level):
        self.listeria_bacteria_level = listeria_bacteria_level

    def get_listeria_bacteria_level(self):
        return self.listeria_bacteria_level

    @staticmethod
    def json_to_class(json_data):
        automates = []

        for json_object in json_data:
            automates.append(Automate(
                json_object["unit_no"],
                json_object["automate_no"],
                json_object["type_automate"],
                json_object["tank_temperature"],
                json_object["ext_temperature"],
                json_object["milk_weight_tank"],
                json_object["final_weight"],
                json_object["ph"],
                json_object["k_plus"],
                json_object["nacl_concentration"],
                json_object["salmonella_bacteria_level"],
                json_object["e_coli_bacteria_level"],
                json_object["listeria_bacteria_level"]))

        return automates
