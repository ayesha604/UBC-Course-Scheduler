import json

from backend.objects.CoursesLoader import CoursesLoader
from backend.objects.Scheduler import Scheduler
from backend.objects.Scraper import Scraper

SAVED_COURSES_PATH = 'backend/saved_json/saved_courses.json'
SAVED_TIMETABLES_PATH = 'backend/saved_json/saved_timetables.json'
TO_LOAD = ['CPSC 110', 'MATH 100']


def main():
    loader = CoursesLoader()
    loader.load(SAVED_COURSES_PATH)
    courses = loader.get_courses_from_names(TO_LOAD)

    scheduler = Scheduler()
    scheduler.schedule(courses, 1)
    data = scheduler.to_dict()
    with open(SAVED_TIMETABLES_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()