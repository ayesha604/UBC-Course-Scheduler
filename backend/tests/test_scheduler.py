# import os
# import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import os
# print(os.getcwd())
from backend.objects.Course import Course
from backend.objects.Scheduler import Scheduler
from backend.objects.Scraper import Scraper
from backend.objects.Timetable import Timetable


# def getMATH100Sections() -> list[Section]:
#     sectionA11 = Section("MATH 100 A11", {"Mon":(1100, 1200)}, 1,\
#         "Biological Sciences", None, [], "Discussion", [])
#     sectionA12 = Section("MATH 100 A12", {"Wed":(900, 1000)}, 1,\
#         "Frederic Lasserre", "Emanuele Bodon", [], "Discussion", [])
#     sectionA13 = Section("MATH 100 A13", {"Wed":(1400, 1500)}, 1,\
#         "Leonard S. Klinck", "Yunhui He", [], "Discussion", [])
#     sectionA14 = Section("MATH 100 A14", {"Thu":(900, 1000)}, 1,\
#         "Mathematics", None, [], "Discussion", [])
#     sectionA15 = Section("MATH 100 A15", {"Thu":(1300, 1400)}, 1,\
#         "P. A. Woodward Instructional Resources Centre", "Yunhui He", [], "Discussion", [])
#     sectionA16 = Section("MATH 100 A16", {"Fri":(1100, 1200)}, 1,\
#         "Mathematics", "Severin Schraven", [], "Discussion", [])
#     section1A1 = Section("MATH 100 1A1", {"Tue":(800, 1000)}, 1,\
#         "Earth Sciences Building", "Anthony Wachs",\
#             [sectionA11, sectionA12, sectionA13, sectionA14, sectionA15, sectionA16],\
#                 "Lecture", ["Discussion"])
#
#     sectionB11 = Section("MATH 100 B11", {"Mon": (900, 1000)}, 1,\
#         "Geography", "Peter Harrington", [], "Discussion", [])
#     sectionB12 = Section("MATH 100 B12", {"Mon": (900, 1000)}, 1,\
#         "Geography", None, [], "Discussion", [])
#     sectionB13 = Section("MATH 100 B13", {"Thu": (1200, 1300)}, 1,\
#         "Geography", "Yifeng Huang", [], "Discussion", [])
#     sectionB14 = Section("MATH 100 B14", {"Thu": (1300, 1400)}, 1,\
#         "Jack Bell Building for the School of Social Work", "Yifeng Huang", [], "Discussion", [])
#     sectionB15 = Section("MATH 100 B15", {"Fri": (1400, 1500)}, 1,\
#         "Leonard S. Klinck", None, [], "Discussion", [])
#     sectionB16 = Section("MATH 100 B16", {"Fri": (1500, 1600)}, 1,\
#         "Geography", "Nicholas Rouse", [], "Discussion", [])
#     sectionB17 = Section("MATH 100 B17", {"Tue": (1100, 1200)}, 1,\
#         "Chemistry", None, [], "Discussion", [])
#     sectionB18 = Section("MATH 100 B18", {"Tue": (1200, 1300)}, 1,\
#         "Chemistry", None, [], "Discussion", [])
#     section1B1 = Section("MATH 100 1B1", {"Wed": (800, 1000)}, 1,\
#         "P. A. Woodward Instructional Resources Centre", "Elyse Yeager",\
#             [sectionB11, sectionB12, sectionB13, sectionB14, sectionB15, sectionB16, sectionB17, sectionB18],\
#                 "Lecture", ["Discussion"])
#
#
#     sectionC11 = Section("MATH 100 C11", {"Mon": (1300, 1400)}, 1,\
#         "Geography", "Yinon Spinka", [], "Discussion", [])
#     sectionC12 = Section("MATH 100 C12", {"Tue": (1000, 1100)}, 1,\
#         "Mathematics", None, [], "Discussion", [])
#     sectionC13 = Section("MATH 100 C13", {"Tue": (1100, 1200)}, 1,\
#         "Mathematics", None, [], "Discussion", [])
#     sectionC14 = Section("MATH 100 C14", {"Wed": (1400, 1500)}, 1,\
#         "P. A. Woodward Instructional Resources Centre", "Brian Wetton", [], "Discussion", [])
#     section1C1 = Section("MATH 100 1C2", {"Thu": (1200, 1400)}, 1,\
#         "P. A. Woodward Instructional Resources Centre", "Brian Wetton",\
#             [sectionC11, sectionC12, sectionC13, sectionC14], "Lecture", ["Discussion"])
#
#     return [section1A1, section1B1, section1C1]
#
# def getPHYS117Sections() -> list[Section]:
#     sectionT1A = Section("PHYS 117 T1A", {"Mon": (1000, 1100)}, 1,\
#         "Hebb", None, [], "Tutorial", [])
#     sectionT1B = Section("PHYS 117 T1B", {"Mon": (1400, 1500)}, 1,\
#         "Hebb", None, [], "Tutorial", [])
#     sectionT1C = Section("PHYS 117 T1C", {"Tue": (1100, 1200)}, 1,\
#         "Hebb", None, [], "Tutorial", [])
#     sectionT1D = Section("PHYS 117 T1D", {"Tue": (1300, 1400)}, 1,\
#         "Hebb", None, [], "Tutorial", [])
#     sectionT1E = Section("PHYS 117 T1E", {"Tue": (1530, 1630)}, 1,\
#         "Hebb", None, [], "Tutorial", [])
#     sectionT1F = Section("PHYS 117 T1F", {"Mon": (1300, 1400)}, 1,\
#         "Hebb", None, [], "Tutorial", [])
#     sectionT1G = Section("PHYS 117 T1G", {"Mon": (1600, 1700)}, 1,\
#         "Hebb", None, [], "Tutorial", [])
#     sectionT1N = Section("PHYS 117 T1N", {"Mon": (1500, 1600)}, 1,\
#         "Hebb", None, [], "Tutorial", [])
#     sectionT1O = Section("PHYS 117 T1O", {"Tue": (1000, 1100)}, 1,\
#         "Hebb", None, [], "Tutorial", [])
#
#     section101 = Section("PHYS 117 101", {"Mon": (1100, 1200),\
#         "Wed": (1100, 1200), "Fri": (1100, 1200)}, 1, "Hebb", "Joss Ives",\
#             [sectionT1A, sectionT1B, sectionT1C, sectionT1D, sectionT1E,\
#                 sectionT1F, sectionT1G, sectionT1N, sectionT1O], "Lecture", ["Tutorial"])
#     section102 = Section("PHYS 117 102", {"Mon": (1500, 1600),\
#         "Wed": (1500, 1600), "Fri": (1500, 1600)}, 1, "Hennings", "Joss Ives",\
#             [sectionT1A, sectionT1B, sectionT1C, sectionT1D, sectionT1E,\
#                 sectionT1F, sectionT1G, sectionT1N, sectionT1O], "Lecture", ["Tutorial"])
#     return [section101, section102]
#
#
# def getPHYS119Sections() -> list[Section]:
#     sectionL1A = Section("PHYS 119 L1A", {"Wed": (1400, 1700)}, 1,\
#         "Hebb", "Carl Michal", [], "Laboratory", [])
#     sectionL1B = Section("PHYS 119 L1B", {"Thu": (930, 1230)}, 1,\
#         "Hebb", "Carl Michal", [], "Laboratory", [])
#     sectionL1D = Section("PHYS 119 L1D", {"Wed": (1100, 1400)}, 1,\
#         "Hebb", "Carl Michal", [], "Laboratory", [])
#     sectionL1F = Section("PHYS 119 L1F", {"Fri": (1400, 1700)}, 1,\
#         "Hebb", "Carl Michal", [], "Laboratory", [])
#
#     sectionL2A = Section("PHYS 119 L2A", {"Tue": (800, 1100)}, 2,\
#         "Hebb", "Joss Ives", [], "Laboratory", [])
#     sectionL2B = Section("PHYS 119 L2B", {"Tue": (1100, 1400)}, 2,\
#         "Hebb", "Joss Ives", [], "Laboratory", [])
#     sectionL2C = Section("PHYS 119 L2C", {"Tue": (1400, 1700)}, 2,\
#         "Hebb", "Alison Lister", [], "Laboratory", [])
#     sectionL2D = Section("PHYS 119 L2D", {"Wed": (1100, 1400)}, 2,\
#         "Hebb", "Alison Lister", [], "Laboratory", [])
#     sectionL2E = Section("PHYS 119 L2E", {"Thu": (1400, 1700)}, 2,\
#         "Hebb", "Alison Lister", [], "Laboratory", [])
#     sectionL2F = Section("PHYS 119 L2F", {"Fri": (1400, 1700)}, 2,\
#         "Hebb", "Alison Lister", [], "Laboratory", [])
#     sectionL2G = Section("PHYS 119 L2G", {"Thu": (800, 1100)}, 2,\
#         "Hebb", "Alison Lister", [], "Laboratory", [])
#
#     return [sectionL1A, sectionL1B, sectionL1D, sectionL1F,\
#         sectionL2A, sectionL2B, sectionL2C, sectionL2D, sectionL2E, sectionL2F, sectionL2G]

if __name__ == "__main__":
    courseToScrape = ['CPSC 110','PHYS 117', 'CPSC 110', 'MATH 100']
    scraper = Scraper()
    scraper.scrape_course_list(courseToScrape)
    # print(scraper.get_courses())

    # math100Sections = getMATH100Sections()
    # phys117Sections = getPHYS117Sections()
    # phys119Sections = getPHYS119Sections()

    # math100 = Course("MATH 100", math100Sections, 3)
    # phys117 = Course("PHYS 117", phys117Sections, 3)
    # phys119 = Course("PHYS 119", phys119Sections, 1)

    coursesToSchedule = list(scraper.get_courses().values())
    # print(coursesToSchedule[1].getCourseName())
    # print(coursesToSchedule[1].getSections())
    scheduler = Scheduler()
    scheduler.schedule(coursesToSchedule, 1)
    timetables = scheduler.getTimetables()

    # print(len(timetables))
    for timetable in timetables[0:100]:
        sections = timetable.getSections()
        for section in sections:
            print(f"{section.name} : {section.times}")
        print()