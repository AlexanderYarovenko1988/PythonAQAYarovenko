class Passenger:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

class TrainCar:
    def __init__(self, number):
        self.number = number
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < 10:
            self.passengers.append(passenger)
        else:
            raise Exception("Train car is full. Cannot add more passengers.")

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        car_info = f'"traincar": "{self.number}",\n'
        passenger_info = ""
        for idx, passenger in enumerate(self.passengers, start=1):
            passenger_info += f'"passenger_name": "{passenger.name}",\n' \
                             f'"destination": "{passenger.destination}",\n' \
                             f'"place": {idx}\n'
        return car_info + passenger_info

class Train:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_locomotive(self):
        if self.cars:
            self.cars.pop(0)
        else:
            raise ValueError("Train has no cars to remove.")

    def __len__(self):
        return len(self.cars)

    def __str__(self):
        train_info = f'"train": "{self.name}",\n'
        car_info = ""
        for car in self.cars:
            car_info += "{" + str(car) + "},\n"
        return train_info + car_info

    def __call__(self, station, exiting_passengers):
        for car in self.cars:
            for passenger in exiting_passengers:
                if passenger in car.passengers:
                    car.passengers.remove(passenger)
                    station.entering_passengers.append(passenger)

class Station:
    def __init__(self, name):
        self.name = name
        self.entering_passengers = []
        self.exiting_passengers = []

    def add_entering_passenger(self, passenger):
        self.entering_passengers.append(passenger)

    def add_exiting_passenger(self, passenger):
        self.exiting_passengers.append(passenger)

    def __str__(self):
        return f'"station": "{self.name}",\n' \
               f'"entering_passengers": {len(self.entering_passengers)},\n' \
               f'"exiting_passengers": {len(self.exiting_passengers)}'

# Приклад використання класів
if __name__ == "__main__":
    # Створюємо пасажирів, вагони, потяг і станції
    passenger1 = Passenger("John Dow", "Station A")
    passenger2 = Passenger("Alice Smith", "Station B")
    car1 = TrainCar(1)
    car2 = TrainCar(2)
    train = Train("Express")
    station_a = Station("Station A")
    station_b = Station("Station B")

    # Додаємо пасажирів до вагонів
    car1.add_passenger(passenger1)
    car2.add_passenger(passenger2)

    # Додаємо вагони до потягу
    train.add_car(car1)
    train.add_car(car2)

    # Потяг прибув на станцію Station A і з нього вийшли 2 пасажири, які їдуть на Station B
    train(station_a, [passenger1, passenger2])

    # Виводимо інформацію про потяг та станції.
    print("Train Information:")
    print(train)

    print("\nStation A Information:")
    print(station_a)

    print("\nStation B Information:")
    print(station_b)
