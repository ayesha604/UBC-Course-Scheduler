from bs4 import BeautifulSoup
import requests

from backend.Course import Course

# sorry ubc
HEADERS = {
    'User-Agent': 'very real human',
    'From': 'human@realperson.com'
}
ALL_DEPS_URL = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-all-departments"
DEP_URL = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-department&dept="


def make_soup(url: str) -> BeautifulSoup:
    page = requests.get(url, headers=HEADERS).content
    return BeautifulSoup(page, "html.parser")


class Scraper:
    courses = {}  # name: Course
    deps = []  # str

    def __init__(self, do_scrape=False):
        if do_scrape:
            self.scrape_all()

    def scrape_all(self):
        ...

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
                self.courses[link.text] = None

    def get_departments(self) -> list[str]:
        return self.deps

    def get_courses(self) -> dict[str:Course]:
        return self.courses
