from typing import Iterator

from data.data import Person
from faker import Faker

faker_ru = Faker("ru_RU")
Faker.seed()


def generated_info_person() -> Iterator[Person]:
    """
    The `generated_info_person` method generates information about a person in the form of a `Person` object.
    Description of the method operation:
    The method uses the `faker_ru` library to generate random data about a person.
    The `yield` method returns a `Person` object with the following attributes:
    - full_name
    - email
    - current_address
    - permanent_address

    :return: generator
    """
    yield Person(
        full_name=f"{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name()}",
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )
