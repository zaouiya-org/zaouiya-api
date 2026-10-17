
from pydantic import BaseModel

from zaouiya.seeding.hardcoded import DEGREE_PROGRAMS
from zaouiya.seeding.factories import AcademicLevelFactory

import json


with open("collections/degree_programs.json", "w") as f:
    json.dump(
        {
            "meta": {
                "collectionName": "degree_programs",
                "aggregated": False,
                "aggregatedBy": None,
            },
            "data": DEGREE_PROGRAMS,
        },
        f,
        indent=2,
    )


with open("collections/pedagogical_structure.json", "w") as f:
    json.dump(
        {
            "meta": {
                "collectionName": "academic_levels",
                "aggregated": True,
                "aggregatedBy": {"model": "Specialty", "field": "acronyme"},
            },
            "data": {
                prg["acronyme"]: AcademicLevelFactory.of_degreeProgram(prg["acronyme"])
                for prg in DEGREE_PROGRAMS
            },
        },
        f,
        indent=2,
        ensure_ascii=False,
        default=lambda o: o.model_dump() if isinstance(o, BaseModel) else str(o)  # pyright: ignore[reportAny]
    )
