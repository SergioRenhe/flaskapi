from models.cars import Car
from models.persons import Person


def test_person_sale_opportunity():
    """
    Test should return true when person has
    less than 3 cars and false otherwise
    """

    person = Person()
    person.save()
    assert person.sale_opportunity
    assert len(person.cars) == 0

    car = Car(owner_id=person.id, color="BLUE", model="SEDAN")
    cars_to_save = 3
    cars = [car for i in range(cars_to_save)]
    Car.bulk_save(cars)
    person = Person.retrieve(person.id)
    assert not person.sale_opportunity
    assert len(person.cars) == 3
