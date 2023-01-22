from backend.Scraper import Scraper

TO_SCRAPE = 'CPSC'


def main():
    s = Scraper()
    # s.scrape_deps()
    # for dep in TO_SCRAPE:
    #     s.scrape_course_names(dep)
    # print(s.get_course_names())
    s.scrape_course('CPSC 110')
    # print(s.get_courses())


if __name__ == '__main__':
    main()
