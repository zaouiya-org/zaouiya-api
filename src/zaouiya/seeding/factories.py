
from zaouiya.seeding.hardcoded import PEDAGOGICAL_STRUCTURE_CFG

from typing import ClassVar, Protocol

from polyfactory.factories.pydantic_factory import ModelFactory

from polyfactory import Use

from polyfactory.fields import PostGenerated

from zaouiya.bases import *

import zaouiya.seeding.generators as gen


class _Buildable(Protocol):
    @classmethod
    def from_cfg(cls, index: int, cfg: dict[str, int]) -> Model: ...


class HierarchicalMixin[M: Model](ModelFactory[M]):
    __is_base_factory__ = True # pyright: ignore[reportUnannotatedClassAttribute]

    __index_type__      = int  # pyright:  ignore[reportUnannotatedClassAttribute]
    __index_field__:     ClassVar[str] | None               = None
    __child_factory__:   ClassVar[type[_Buildable]] | None  = None
    __child_field__:     ClassVar[str] | None               = None
    __child_count_key__: ClassVar[str] | None               = None

    @classmethod
    def from_cfg(cls, index: int | str, cfg: dict[str, int]) -> M:
        kwargs: dict[str, object] = {}

        if cls.__index_field__:
            kwargs[cls.__index_field__] = cls.__index_type__(index)

        if (
            cls.__child_factory__
            and cls.__child_field__
            and cls.__index_type__
            and cls.__child_count_key__
        ):
            kwargs[cls.__child_field__] = [
                cls.__child_factory__.from_cfg(i, cfg)
                for i in range(1, cfg[cls.__child_count_key__]+1)
            ]

        return cls.build(**kwargs, factory_use_construct = False)


class StudentFactory(HierarchicalMixin[StudentBase]):
    name: Use[[], str] = Use(gen.fake.first_name)
    surname : Use[[], str] = Use(gen.fake.last_name)
    matricule : Use[[], str] = Use(gen.matricule)
    email : PostGenerated = PostGenerated(gen.email)


class GroupFactory(HierarchicalMixin[GroupBase]):
    __index_field__ = "number"                             # pyright: ignore[reportUnannotatedClassAttribute]
    __child_factory__ = StudentFactory                     # pyright: ignore[reportUnannotatedClassAttribute]
    __child_field__ = "students"                           # pyright: ignore[reportUnannotatedClassAttribute]
    __child_count_key__ = "nb_students_per_group"          # pyright: ignore[reportUnannotatedClassAttribute]


class SectionFactory(HierarchicalMixin[SectionBase]):
    __index_type__ = str                                   # pyright: ignore[reportUnannotatedClassAttribute]
    __index_field__ = "identifier"                         # pyright: ignore[reportUnannotatedClassAttribute]
    __child_factory__ = GroupFactory                       # pyright: ignore[reportUnannotatedClassAttribute]
    __child_field__ = "groups"                             # pyright: ignore[reportUnannotatedClassAttribute]
    __child_count_key__ = "nb_groups_per_section"          # pyright: ignore[reportUnannotatedClassAttribute]


class AcademicLevelFactory(HierarchicalMixin[AcademicLevelBase]):
    __index_field__ = "level"                              # pyright: ignore[reportUnannotatedClassAttribute]
    __child_factory__ = SectionFactory                     # pyright: ignore[reportUnannotatedClassAttribute]
    __child_field__ = "sections"                           # pyright: ignore[reportUnannotatedClassAttribute]
    __child_count_key__ = "nb_sections_per_academicLevel"  # pyright: ignore[reportUnannotatedClassAttribute]

    @staticmethod
    def of_degreeProgram(degreeProgram_acroyme: str) -> list[AcademicLevelBase]:
        return [
            AcademicLevelFactory.from_cfg(index=i, cfg=cfg)
            for i, cfg in enumerate(
                PEDAGOGICAL_STRUCTURE_CFG[degreeProgram_acroyme],
                start=1
            )
        ]
