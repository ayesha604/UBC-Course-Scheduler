import json

from backend.objects.Scraper import Scraper

COURSES_TO_SCRAPE = ['CPSC 110', 'MATH 100', 'PHYS 117', 'CPSC 121',
                     'PHYS 119', 'MATH 101']
PATH = './saved_json/saved_courses.json'


def main():
    scraper = Scraper()
    scraper.set_course_names(COURSES_TO_SCRAPE)
    scraper.scrape_all_courses()
    courses = scraper.get_courses()

    to_save = []
    for course in courses.values():
        to_save.append(course.to_dict())
    data = {"data": to_save}

    with open(PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()

