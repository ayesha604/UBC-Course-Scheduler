from backend.Scraper import Scraper


def main():
    s = Scraper()
    print(s.scrape_deps())


if __name__ == '__main__':
    main()
