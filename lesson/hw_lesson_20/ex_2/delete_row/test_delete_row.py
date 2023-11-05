import csv
import os
import pytest
from delete_row import delete_row

@pytest.fixture
def sample_csv_file():
    filename = 'test_delete_example.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Elizabet,Fork,19,Female,3000'])
        writer.writerow(['Reginald,Lidoo,42,Male,2500'])
        writer.writerow(['Elizabet,Fork,19,Female,3001'])
        writer.writerow(['Reginald,Lidoo,42,Male,2501'])
    yield filename
    os.remove(filename)

def test_delete_row(sample_csv_file):
    with open(sample_csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        initial_row_count = len(list(reader))

    delete_row(sample_csv_file, 1)

    with open(sample_csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        final_row_count = len(list(reader))

    assert initial_row_count - 1 == final_row_count
