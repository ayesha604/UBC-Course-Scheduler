from bs4 import BeautifulSoup
from urllib.request import urlopen

# Constants
DEPS_URL = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-all-departments"


class Scraper:
    courses = {}

    def __init__(self, do_scrape=False):
        if do_scrape:
            self.scrape_all()

    def scrape_all(self):
        ...

    def scrape_deps(self):
        page = urlopen(DEPS_URL)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        entries = soup.find_all("tr")
        return entries

