
from sqlmodel import SQLModel

# -------------- PEDAGOGICAL STRUCTURE --------------

class StudentBase(SQLModel):
    surname: str
    name: str
    matricule: str
    email: str


class GroupBase(SQLModel):

    number: int
    students: list[StudentBase]


class SectionBase(SQLModel):
    identifier: str

    groups: list[GroupBase]


class AcademicLevelBase(SQLModel):
    level: int

    sections: list[SectionBase]


class DegreeProgramBase(SQLModel):
    name: str
    acronyme: str
    cycle: str


# -------------- ACADEMIC STRUCTURE --------------


class CourseBase(SQLModel):
    name: str


class SemesterCoursesBase(SQLModel):

    hasTD: bool
    hasTP: bool

    numTD: int
    numTP: int

    coef: int

    course: CourseBase


class SemesterBase(SQLModel):
    number: int

    courses: list[SemesterCoursesBase]


class CourseTeacherBase(SQLModel):
    course: CourseBase
    section: SectionBase


class CourseAssistantBase(SQLModel):
    role: str

    course: CourseBase
    group: GroupBase


class ProfessorBase(SQLModel):
    surname: str
    name: str
    email: str
    phoneNumber: str

    teacherCourses: list[CourseTeacherBase]
    assistingCourses: list[CourseAssistantBase]


type Model = ( StudentBase
              | GroupBase
              | SectionBase
              | AcademicLevelBase
              | DegreeProgramBase
              | CourseBase
              | SemesterBase
              | SemesterCoursesBase
              | ProfessorBase
              | CourseTeacherBase
              | CourseAssistantBase )
