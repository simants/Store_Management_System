import os
import random
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.helper.data_creation_helper import DataCreationHelper
from store_management_systems.commons.generic_constants import GenericConstants


class ExpenseDataCreation(DataCreationHelper):
    def __init__(self):
        super().__init__()
        self.data_count = 200
        self.mop = ['Card', 'Cash']
        self.select_expense_category_query = "SELECT id " \
                                             "FROM S22_S003_11_EXPENSE_CATEGORY"

        self.insert_expense_query = "INSERT INTO S22_S003_11_EXPENSE " \
                                    "(category_id, amount, mode_of_payment, store_id, created_at, updated_at) " \
                                    "values " \
                                    "({0}, {1}, '{2}', {3}, (SYSDATE, 'MM-DD-YYYY HH24:MI:SS'), " \
                                    "(SYSDATE, 'MM-DD-YYYY HH24:MI:SS'));"

        self.select_store_query = "SELECT id " \
                                  "FROM S22_S003_11_STORE " \
                                  "ORDER BY id asc"

    def create_data(self):
        expense_categories = self.get_expense_categories()
        store_ids = self.get_store_ids()
        f = self.get_file_obj(GenericConstants.INSERT_EXPENSE_QUERIES_FILE)
        self.insert_expense_data(store_ids, expense_categories, f)

    def get_expense_categories(self):
        self.cur.execute(self.select_expense_category_query)
        rows = self.cur.fetchall()
        return rows

    def insert_expense_data(self, store_ids, expense_categories, f):
        i = 0
        while i < self.data_count:
            for store_id in store_ids:
                for category_id in expense_categories:
                    amount = round(random.uniform(100.00, 1000.00), 2)
                    insert_query = self.insert_expense_query.format(
                        category_id[0], amount, random.choice(self.mop).upper(), store_id[0])
                    f.write(insert_query + "\n")
                    i += 1
        f.close()


if __name__ == '__main__':
    ExpenseDataCreation().create_data()
