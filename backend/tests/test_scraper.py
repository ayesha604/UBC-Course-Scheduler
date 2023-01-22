from backend.Scraper import Scraper

TO_SCRAPE = ['CPSC 110']


def main():
    s = Scraper()
    # s.scrape_deps()
    # for dep in TO_SCRAPE:
    #     s.scrape_course_names(dep)
    # print(s.get_course_names())
    s.set_course_names(TO_SCRAPE)
    s.scrape_all_courses()
    print(s.courses['CPSC 110'])
    # print(s.get_courses())


if __name__ == '__main__':
    main()
