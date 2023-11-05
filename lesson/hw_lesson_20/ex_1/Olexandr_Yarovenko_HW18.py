import json
import csv


class JSONConverter:
    def __init__(self):
        self.__data = []

    def read_file(self, filename: str):
        with open(filename, 'r') as json_file:
            self.__data = json.load(json_file)

    def write_file(self, filename: str):
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['first_name', 'last_name', 'age', 'gender', 'salary'])
            writer.writeheader()
            for row in self.__data:
                writer.writerow(row)


converter = JSONConverter()
converter.read_file('example.json')
converter.write_file('example.csv')
