import json


class CoursesLoader:
    def __init__(self):
        self.courses = {}

    def load(self, path: str):
        """Load courses from a JSON file."""
        with open(path) as f:
            self.courses = json.load(f)

    def get_course_names(self) -> list[str]:
        return list(self.courses.keys())
