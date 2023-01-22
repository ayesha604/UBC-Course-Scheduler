import json

from backend.objects.Scraper import Scraper

COURSES_TO_SCRAPE = ['CPSC 110', 'MATH 100', 'PHYS 117', 'CPSC 121', 'MATH 101', 'COGS 200']
PATH = './backend/saved_json/saved_courses.json'


def main():
    scraper = Scraper()
    scraper.scrape_course_list(COURSES_TO_SCRAPE)
    courses = scraper.get_courses()

    data = {}
    for (course_name, course) in courses.items():
        data[course_name] = course.to_dict()

    with open(PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()

