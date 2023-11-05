import csv
import os


def delete_row(file_name, row_index):
    with open(file_name, 'r', newline='') as file, open('temp.csv', 'w', newline='') as temp_file:
        reader = csv.reader(file)
        writer = csv.writer(temp_file)

        for i, row in enumerate(reader):
            if i != row_index:
                writer.writerow(row)

    os.replace('temp.csv', file_name)


delete_row('../add_row/example.csv', 1)
