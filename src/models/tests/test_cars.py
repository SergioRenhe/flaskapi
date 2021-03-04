import pytest

from models.cars import Car
from models.persons import Person


def test_max_cars():
    """
    Test should not let create more
    than 3 cars per person
    """

    person = Person()
    person.save()
    car = Car(owner_id=person.id, color="BLUE", model="SEDAN")
    cars_to_save = 3
    cars = [car for i in range(cars_to_save)]
    Car.bulk_save(cars)
    assert len(person.cars) == 3
    with pytest.raises(Exception):
        car.save()
