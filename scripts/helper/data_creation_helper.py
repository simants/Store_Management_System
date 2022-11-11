from pathlib import Path

import cx_Oracle


class DataCreationHelper:
    def __init__(self):
        connection = cx_Oracle.connect("sxk0371", "Shelby199625", "acaddbprod.uta.edu:1523/pcse1p.data.uta.edu")
        self.cur = connection.cursor()
        self.select_store_id_query = "SELECT id " \
                                     "FROM S22_S003_11_STORE " \
                                     "ORDER BY id asc"

        self.select_store_id_zipcode_query = "SELECT id, zipcode " \
                                             "FROM S22_S003_11_STORE " \
                                             "ORDER BY id asc"

    def get_store_ids(self):
        self.cur.execute(self.select_store_id_query)
        rows = self.cur.fetchall()
        return rows

    @staticmethod
    def get_file_obj(file_name):
        if Path(file_name).exists():
            open(file_name, 'w').close()
        return open(file_name, 'a')

    def get_store_ids_zipcode(self):
        self.cur.execute(self.select_store_id_zipcode_query)
        rows = self.cur.fetchall()
        return rows
