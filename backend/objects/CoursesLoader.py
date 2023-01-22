import json

from backend.objects.Course import Course
from backend.objects.Section import Section


def course_from_dict(course_dict: dict) -> Course:
    name = course_dict['name']
    sections = []
    for section in course_dict['sections']:
        sections.append(section_from_dict(section))
    requirements = course_dict['requirements']
    creds = course_dict['credits']
    return Course(name, sections, requirements, creds)


def section_from_dict(section_dict: dict) -> Section:
    # why
    status = section_dict['status']
    name = section_dict['name']
    activity = section_dict['activity']
    term = section_dict['term']
    mode = section_dict['mode']
    times = section_dict['times']
    location = section_dict['location']
    professor = section_dict['professor']
    dependencies = section_dict['dependencies']

    dep_list = []
    if dependencies is not None:
        for dep_dict in dependencies:
            dep = section_from_dict(dep_dict)
            dep_list.append(dep)

    return Section(status, name, activity, term, mode, times,
                   location, professor, dep_list)


class CoursesLoader:
    def __init__(self):
        self.courses = {}

    def load(self, path: str):
        """Load courses from a JSON file."""
        with open(path) as f:
            self.courses = json.load(f)

    def get_course_names(self) -> list[str]:
        """Return all loaded course names"""
        return list(self.courses.keys())

    def get_course_names_term(self, term: int) -> list[str]:
        """Return all loaded course names for given term"""
        allCourses = list(self.courses.values()) # listof Course object
        courseNamesInTerm = []

        for course in allCourses:
            for s in course.getSections():
                if s.term == term:
                    courseNamesInTerm.append(course.getName())
                    break

        return courseNamesInTerm

    def get_courses_from_names(self, names: list[str]) -> list[Course]:
        """Get a list of Course objects from names"""
        courses = []
        for name in names:
            if name in self.courses.keys():
                courses.append(course_from_dict(self.courses[name]))
            else:
                raise KeyError(f'Could not find course {name}')
        return courses
