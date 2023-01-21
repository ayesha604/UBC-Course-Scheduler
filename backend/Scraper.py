from bs4 import BeautifulSoup
import requests

HEADERS = {
    'User-Agent': 'very real human',
    'From': 'human@realperson.com'
}
DEPS_URL = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-all-departments"


def make_soup(url: str) -> BeautifulSoup:
    page = requests.get(url, headers=HEADERS).content
    return BeautifulSoup(page, "html.parser")


class Scraper:
    courses = {}
    deps = []

    def __init__(self, do_scrape=False):
        if do_scrape:
            self.scrape_all()

    def scrape_all(self):
        ...

    def scrape_deps(self):
        new_deps = []
        soup = make_soup(DEPS_URL)
        for link in soup.find_all('a'):
            if link.parent.name == 'td':
                new_deps.append(link.text)
        self.deps = new_deps

    def get_departments(self):
        return self.deps

    def get_courses(self):
        return self.courses

