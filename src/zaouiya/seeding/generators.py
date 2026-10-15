
import random

from typing import Any

from zaouiya.seeding.hardcoded import DEGREE_PROGRAMS, STUDENTS_DISTRIBUTION

import faker

fake = faker.Faker("fr_DZ")


def gen_matricule():
    return str(random.randint(100_000_000_000, 999_999_999_999))


def gen_phoneNumber():
    return (
        "0"
        + random.choice(["5", "6", "7"])
        + str(random.randint(10_000_000, 99_999_999))
    )


def gen_academicLevels(_name: str, values: dict[str, object], **_kwargs: dict[str, object]):
    for i, al in enumerate(STUDENTS_DISTRIBUTION[values["cycle"]]["academicLevels"]):
        pass
