from backend.objects.Course import Course
from backend.objects.Scheduler import Scheduler
from backend.objects.Scraper import Scraper
from backend.objects.Timetable import Timetable

if __name__ == "__main__":
    courseToScrape = ['CPSC 110', 'CPSC 121']
    scraper = Scraper()
    scraper.scrape_course_list(courseToScrape)

    coursesToSchedule = list(scraper.get_courses().values())
    scheduler = Scheduler()
    scheduler.schedule(coursesToSchedule, 2)
    timetables = scheduler.getTimetables()

    # print(len(timetables))
    print("#### Top 3 Timetable ###")
    for timetable in scheduler.getTopTimetables():
        sections = timetable.getSections()
        print(f"Timetable with score {timetable.getScore()}")
        for section in sections:
            print(f"{section.name} : {section.times}")
        print()
    print("#### Worst 3 Timetable ###")
    for timetable in scheduler.getWorstTimetables():
        sections = timetable.getSections()
        print(f"Timetable with score {timetable.getScore()}")
        for section in sections:
            print(f"{section.name} : {section.times}")
        print()