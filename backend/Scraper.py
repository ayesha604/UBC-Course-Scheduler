import bs4
from bs4 import BeautifulSoup
import requests
import time

from backend.NewSection import Section
from backend.Course import Course

# sorry ubc
HEADERS = {
    'User-Agent': 'very real human',
    'From': 'human@realperson.com'
}
ALL_DEPS_URL = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-all-departments"
DEP_URL = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-department&dept="
COURSE_URL = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept="
COURSE_URL_ADD = "&course="
SLEEP_TIME = 0.5


def make_soup(url: str) -> BeautifulSoup:
    page = requests.get(url, headers=HEADERS).content
    return BeautifulSoup(page, "lxml")


def is_lecture(tag: bs4.Tag):
    return tag.has_attr('class') and tag['class'] == ['section1'] and "Lecture" in tag.text


def is_section(tag: bs4.Tag) -> bool:
    return tag.name == 'tr' and tag.has_attr('class')


def make_section(tag: bs4.Tag) -> Section:
    subs = list(tag.children)
    status = subs[0].text
    name = subs[1].a.text
    activity = subs[2].text
    term = int(subs[3].text)
    mode = subs[4].text.strip()

    days = subs[6].text.strip()
    start_time = int(subs[7].text.replace(':', ''))
    end_time = int(subs[8].text.replace(':', ''))

    times = {}
    for day in days.split():
        times[day] = (start_time, end_time)

    # print(status, name, activity, term, mode, times)
    return Section(status, name, activity, term, mode, times)


def scrape_course(course_name: str) -> Course:
    """
    Scrape a Course object from a course name.

    Assumes that lectures are main courses, and every non-lecture underneath them
    is a dependency for that lecture section.
    """
    department, number = course_name.split(" ")
    url = COURSE_URL + department + COURSE_URL_ADD + number
    soup = make_soup(url)
    print(url)

    sections = []

    lecture_tags = soup.find_all(is_lecture)
    for lecture_tag in lecture_tags:
        lecture_section = make_section(lecture_tag)
        dependencies = []
        next_tag = lecture_tag.next_sibling
        while type(next_tag) == bs4.Tag and next_tag.has_attr('class') and next_tag['class'] == ['section2']:
            dependencies.append(make_section(next_tag))
            next_tag = next_tag.next_sibling
        lecture_section.dependencies = dependencies
        sections.append(lecture_section)

    return Course(course_name, sections, None)


class Scraper:
    courses = {}  # name: Course
    deps = []  # str
    course_names = []

    def __init__(self, do_scrape=False):
        if do_scrape:
            self.scrape_all()

    def scrape_all(self):
        print('Scraping all department names...')
        self.scrape_deps()
        print(self.deps)
        num_done = 0
        for dep in self.deps:
            print(f'\rScraping all course names... {num_done} / {len(self.deps)}', end='')
            self.scrape_course_names(dep)
            time.sleep(SLEEP_TIME)
            num_done += 1
        print()

    def scrape_deps(self):
        new_deps = []
        soup = make_soup(ALL_DEPS_URL)
        for link in soup.find_all('a'):
            if link.parent.name == 'td':
                new_deps.append(link.text)
        self.deps = new_deps

    def scrape_course_names(self, dep: str):
        url = DEP_URL + dep
        soup = make_soup(url)
        for link in soup.find_all('a'):
            if link.parent.name == 'td':
                if link.text not in self.course_names:
                    self.course_names.append(link.text)

    def scrape_all_courses(self):
        for course_name in self.course_names:
            self.courses[course_name] = scrape_course(course_name)

    def get_departments(self) -> list[str]:
        return self.deps

    def get_courses(self) -> dict[str:Course]:
        return self.courses

    def get_course_names(self) -> list[str]:
        return self.course_names

    def set_course_names(self, course_names: list[str]):
        self.course_names = course_names.copy()