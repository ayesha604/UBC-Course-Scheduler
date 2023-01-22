import bs4
from bs4 import BeautifulSoup
import requests
import time

from backend.objects.NewSection import Section
from backend.objects.Course import Course

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
    return tag.has_attr('class') and tag['class'] == ['section1'] \
        and "Lecture" in tag.text and "STT" not in tag.text


def is_section(tag: bs4.Tag) -> bool:
    return tag.name == 'tr' and tag.has_attr('class')


def is_dependent(tag: bs4.Tag) -> bool:
    return tag.has_attr('class') and tag['class'] == ['section2'] and \
        "Waiting List" not in tag.text


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
    # print(url)

    sections = []
    # list of unique activities
    requirements = []

    lecture_tags = soup.find_all(is_lecture)
    for lecture_tag in lecture_tags:
        lecture_section = make_section(lecture_tag)
        dependencies = []
        next_tag = lecture_tag.next_sibling
        while type(next_tag) == bs4.Tag and is_dependent(next_tag):
            new_dep = make_section(next_tag)
            if new_dep.activity not in requirements:
                requirements.append(new_dep.activity)
            dependencies.append(new_dep)
            next_tag = next_tag.next_sibling
        lecture_section.dependencies = dependencies
        sections.append(lecture_section)

    return Course(course_name, sections, requirements, None)


class Scraper:
    _courses = {}  # name: Course
    _deps = []  # str
    _course_names = []

    def __init__(self, do_scrape=False):
        if do_scrape:
            self.scrape_all()

    def scrape_all(self):
        """TODO: Automatically scrape all courses from the SSC."""
        print('Scraping all department names...')
        self._scrape_deps()
        print(self._deps)
        num_done = 0
        for dep in self._deps:
            print(f'\rScraping all course names... {num_done} / {len(self._deps)}', end='')
            self.scrape_all_from_dep(dep)
            time.sleep(SLEEP_TIME)
            num_done += 1
        print()

    def scrape_course_list(self, course_names: list[str]):
        """Scrape all course names in a list"""
        for course_name in course_names:
            self.scrape_course(course_name)

    def scrape_course(self, course_name: str):
        """Scrape one course name"""
        if course_name not in self._course_names:
            self._course_names.append(course_name)
        self._courses[course_name] = scrape_course(course_name)

    def scrape_all_from_dep(self, dep: str):
        """Scrape all courses from a given department name"""
        url = DEP_URL + dep
        soup = make_soup(url)
        for link in soup.find_all('a'):
            if link.parent.name == 'td':
                if link.text not in self._course_names:
                    self.scrape_course(link.text)

    def _scrape_deps(self):
        new_deps = []
        soup = make_soup(ALL_DEPS_URL)
        for link in soup.find_all('a'):
            if link.parent.name == 'td':
                new_deps.append(link.text)
        self._deps = new_deps

    def get_departments(self) -> list[str]:
        return self._deps

    def get_courses(self) -> dict[str:Course]:
        return self._courses

    def get_course_names(self) -> list[str]:
        return self._course_names
