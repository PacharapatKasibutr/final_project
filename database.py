# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv, os
import copy
class Readfile:
    def __init__(self):
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
    def read_file(self, file):
        file_list = []
        with open(os.path.join(self.__location__, file)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                file_list.append(dict(r))
        return file_list

# add in code for a Database class
class Database:
    def __init__(self):
        self.database = []
    def insert(self, table):
        self.database.append(table)
    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None



# add in code for a Table class
class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def join(self, other_table, common_key):
        joined_table = Table(f"{self.table_name} and {other_table}", [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        filtered_table = Table(f"{self.table_name}_filtered", [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table


    def __is_float(element):
        if element is None:
            return False
        try:
            float(element)
            return True
        except ValueError:
            return False

    def aggregate(self, function, aggregation_key):

        temps = []
        for item1 in self.table:
            if self.__is_float(item1[aggregation_key]):
                temps.append(float(item1[aggregation_key]))
            else:
                temps.append(item1[aggregation_key])
        return function(temps)

    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps


    def insert(self, new_dict):
        self.table.append(new_dict)


    def update(self, user_id, key, value):
        for i in self.table:
            if i['id'] == user_id:
                index = self.table.index(i)
                self.table[index][key] = value


