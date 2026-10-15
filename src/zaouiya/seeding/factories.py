
from polyfactory.factories.pydantic_factory import ModelFactory

from polyfactory import Use

from polyfactory.fields import PostGenerated

from zaouiya.bases import *

from zaouiya.seeding.generators import fake, gen_matricule, gen_academicLevels
from zaouiya.seeding.hardcoded import DEGREE_PROGRAMS, STUDENTS_DISTRIBUTION


class StudentFactory(ModelFactory[StudentBase]):
    name = Use(fake.first_name)
    surname = Use(fake.last_name)
    matricule = Use(gen_matricule)
    email = Use(fake.email)


class GroupFactory(ModelFactory[GroupBase]):
    number: int


class AcademicLevelFactory(ModelFactory[AcademicLevelBase]):
    pass


class DegreeProgramFactory(ModelFactory[DegreeProgramBase]):
    name = Use(next, (program["name"] for program in DEGREE_PROGRAMS))
    acronyme = Use(next, (program["acronyme"] for program in DEGREE_PROGRAMS))
    cycle = Use(next, (program["cycle"] for program in DEGREE_PROGRAMS))

    academicLevels = PostGenerated(gen_academicLevels)
