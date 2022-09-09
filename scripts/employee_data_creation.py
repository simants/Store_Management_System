import os
import random
import string
import sys

import random_address
import names

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.helper.data_creation_helper import DataCreationHelper
from store_management_systems.commons.generic_constants import GenericConstants


class EmployeeDataCreation(DataCreationHelper):
    def __init__(self):
        super().__init__()
        self.data_count = 40
        self.select_store_query = "SELECT id " \
                                  "FROM S22_S003_11_STORE " \
                                  "ORDER BY id asc"

        self.insert_employee_query = "INSERT INTO S22_S003_11_EMPLOYEE " \
                                     "(NAME, SSN, email, phone_no, address_1, address_2, city, state, zipcode, " \
                                     "store_id, created_at, updated_at) " \
                                     "values " \
                                     "('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', {9}, " \
                                     "(SYSDATE, 'MM-DD-YYYY HH24:MI:SS'), (SYSDATE, 'MM-DD-YYYY HH24:MI:SS'));"

    def create_data(self):
        store_ids = self.get_store_ids()
        f = self.get_file_obj(GenericConstants.INSERT_EMPLOYEE_QUERIES_FILE)
        self.insert_employee_data(store_ids, f)

    def insert_employee_data(self, store_ids_zipcode, f):
        i = 0
        ssn_choices = string.ascii_uppercase + string.digits
        while i < self.data_count:
            for store_id in store_ids_zipcode:
                f_name = names.get_first_name()
                l_name = names.get_last_name()
                full_name = f"{f_name} {l_name}"
                ssn = ''.join(random.sample(ssn_choices, len(ssn_choices))[:10])
                email = f"{l_name}.{f_name}@gmail.com"
                phone_no = random.randint(7000000000, 9999999999)
                address = random_address.real_random_address_by_state('CA')
                insert_query = self.insert_employee_query.format(
                    full_name, ssn, email, phone_no, address['address1'], address['address2'], address['city'],
                    address['state'], address['postalCode'], store_id[0]
                )
                f.write(insert_query+"\n")
                i += 1
        f.close()


if __name__ == '__main__':
    EmployeeDataCreation().create_data()
