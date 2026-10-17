
import random

from typing import Any

from zaouiya.seeding.hardcoded import DEGREE_PROGRAMS, PEDAGOGICAL_STRUCTURE_CFG

import faker

fake = faker.Faker("fr_DZ")


def matricule():
    return str(random.randint(100_000_000_000, 999_999_999_999))


def phoneNumber():
    return (
        "0"
        + random.choice(["5", "6", "7"])
        + str(random.randint(10_000_000, 99_999_999))
    )


def email(_name: str, values: dict[str, object], **_kwargs: dict[str, object]):
    return str(values["name"]).lower() \
            + "." + str(values["surname"]).lower() \
            + "@example.com"
