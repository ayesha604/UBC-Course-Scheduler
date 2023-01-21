from backend.Scraper import Scraper


def main():
    s = Scraper()
    s.scrape_deps()
    print(s.get_departments())


if __name__ == '__main__':
    main()
