import pytest

from Olexandr_Yarovenko_HW17 import Passenger, TrainCar, Train, Station

@pytest.fixture
def passenger():
    return Passenger("John Dow", "Station A")

@pytest.fixture
def train_car():
    return TrainCar(1)

@pytest.fixture
def train():
    return Train("Express")

@pytest.fixture
def station():
    return Station("Station A")

@pytest.mark.smoke
class TestTrainCar:

    def test_add_passenger_to_empty_car(self, train_car, passenger):
        train_car.add_passenger(passenger)

        assert len(train_car.passengers) == 1
        assert passenger in train_car.passengers

    @pytest.mark.smoke
    def test_add_passenger_to_full_car(self, train_car, passenger):
        for _ in range(10):
            train_car.add_passenger(passenger)
        with pytest.raises(Exception):
            train_car.add_passenger(passenger)

    def test_remove_passenger_from_car(self, train_car, passenger):
        train_car.add_passenger(passenger)
        train_car.passengers.remove(passenger)
        assert len(train_car.passengers) == 0
        assert passenger not in train_car.passengers

@pytest.mark.smoke
class TestTrain:

    def test_add_car(self, train, train_car):
        train.add_car(train_car)

        assert len(train.cars) == 1
        assert train_car in train.cars

    @pytest.mark.regression
    def test_remove_locomotive(self, train, train_car):
        train.add_car(train_car)
        train.remove_locomotive()
        assert len(train) == 0

    def test_remove_multiple_cars(self, train, train_car):
        for _ in range(5):
            train.add_car(train_car)
        assert len(train) == 5
        for _ in range(3):
            train.remove_locomotive()
        assert len(train) == 2

@pytest.mark.regression
class TestStation:

    def test_add_entering_passenger(self, station, passenger):
        station.add_entering_passenger(passenger)

        assert len(station.entering_passengers) == 1
        assert passenger in station.entering_passengers

    @pytest.mark.regression
    def test_add_exiting_passenger(self, station, passenger):
        station.add_exiting_passenger(passenger)
        assert len(station.exiting_passengers) == 1
        assert passenger in station.exiting_passengers

    def test_remove_entering_passenger(self, station, passenger):
        station.add_entering_passenger(passenger)
        station.entering_passengers.remove(passenger)
        assert len(station.entering_passengers) == 0
        assert passenger not in station.entering_passengers

@pytest.mark.regression
class TestPassenger:

    @pytest.mark.parametrize("name, destination", [("John Dow", "Station A"), ("Alice Smith", "Station B")])
    def test_init(self, name, destination):
        passenger = Passenger(name, destination)

        assert passenger.name == name
        assert passenger.destination == destination

    def test_update_name(self, passenger):
        passenger.name = "Bob Smith"
        assert passenger.name == "Bob Smith"

    def test_update_destination(self, passenger):
        passenger.destination = "Station C"
        assert passenger.destination == "Station C"
