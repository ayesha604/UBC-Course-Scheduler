from backend.Scraper import Scraper


def main():
    s = Scraper()
    s.scrape_deps()
    print(s.get_departments())
    s.scrape_course_names("CPSC")
    print(s.get_courses())


if __name__ == '__main__':
    main()
