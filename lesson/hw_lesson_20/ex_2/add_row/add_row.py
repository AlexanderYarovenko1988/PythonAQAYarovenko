import csv

def add_row(filename, first_name, last_name, age, gender, salary):
    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow([first_name, last_name, age, gender, salary])


if __name__ == "__main__":
    add_row("example.csv", "John", "Doe", 30, "male", 1300000)
