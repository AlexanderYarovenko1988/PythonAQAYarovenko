import csv
import pytest

from add_row import add_row


@pytest.fixture
def filename():
    return "example_test.csv"


def test_add_row(filename):
    add_row(filename, "John", "Doe", 30, "male", 800000)

    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    assert rows[-1] == ["John", "Doe", "30", "male", "800000"]
