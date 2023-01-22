import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Course import Course
from Scheduler import Scheduler
from Section import Section
from Timetable import Timetable

def getMATH100Sections() -> list[Section]:
    sectionA11 = Section("MATH 100 A11", {"Mon":(1100, 1200)}, 1,\
        "Biological Sciences", None, [])
    sectionA12 = Section("MATH 100 A12", {"Wed":(900, 1000)}, 1,\
        "Frederic Lasserre", "Emanuele Bodon", [])
    sectionA13 = Section("MATH 100 A13", {"Wed":(1400, 1500)}, 1,\
        "Leonard S. Klinck", "Yunhui He", [])
    sectionA14 = Section("MATH 100 A14", {"Thu":(900, 1000)}, 1,\
        "Mathematics", None, [])
    sectionA15 = Section("MATH 100 A15", {"Thu":(1300, 1400)}, 1,\
        "P. A. Woodward Instructional Resources Centre", "Yunhui He", [])
    sectionA16 = Section("MATH 100 A16", {"Fri":(1100, 1200)}, 1,\
        "Mathematics", "Severin Schraven", [])
    section1A1 = Section("MATH 100 1A1", {"Tue":(800, 1000)}, 1,\
        "Earth Sciences Building", "Anthony Wachs",\
            [sectionA11, sectionA12, sectionA13, sectionA14, sectionA15, sectionA16])
    
    sectionB11 = Section("MATH 100 B11", {"Mon": (900, 1000)}, 1,\
        "Geography", "Peter Harrington", [])
    sectionB12 = Section("MATH 100 B12", {"Mon": (900, 1000)}, 1,\
        "Geography", None, [])
    sectionB13 = Section("MATH 100 B13", {"Thu": (1200, 1300)}, 1,\
        "Geography", "Yifeng Huang", [])
    sectionB14 = Section("MATH 100 B14", {"Thu": (1300, 1400)}, 1,\
        "Jack Bell Building for the School of Social Work", "Yifeng Huang", [])
    sectionB15 = Section("MATH 100 B15", {"Fri": (1400, 1500)}, 1,\
        "Leonard S. Klinck", None, [])
    sectionB16 = Section("MATH 100 B16", {"Fri": (1500, 1600)}, 1,\
        "Geography", "Nicholas Rouse", [])
    sectionB17 = Section("MATH 100 B17", {"Tue": (1100, 1200)}, 1,\
        "Chemistry", None, [])
    sectionB18 = Section("MATH 100 B18", {"Tue": (1200, 1300)}, 1,\
        "Chemistry", None, [])
    section1B1 = Section("MATH 100 1B1", {"Wed": (800, 1000)}, 1,\
        "P. A. Woodward Instructional Resources Centre", "Elyse Yeager",\
            [sectionB11, sectionB12, sectionB13, sectionB14, sectionB15, sectionB16, sectionB17, sectionB18])


    sectionC11 = Section("MATH 100 C11", {"Mon": (1300, 1400)}, 1,\
        "Geography", "Yinon Spinka", [])
    sectionC12 = Section("MATH 100 C12", {"Tue": (1000, 1100)}, 1,\
        "Mathematics", None, [])
    sectionC13 = Section("MATH 100 C13", {"Tue": (1100, 1200)}, 1,\
        "Mathematics", None, [])
    sectionC14 = Section("MATH 100 C14", {"Wed": (1400, 1500)}, 1,\
        "P. A. Woodward Instructional Resources Centre", "Brian Wetton", [])
    section1C1 = Section("MATH 100 1C2", {"Thu": (1200, 1400)}, 1,\
        "P. A. Woodward Instructional Resources Centre", "Brian Wetton",\
            [sectionC11, sectionC12, sectionC13, sectionC14])
    
    return [section1A1, section1B1, section1C1]

def getPHYS117Sections() -> list[Section]:
    sectionT1A = Section("PHYS 117 T1A", {"Mon": (1000, 1100)}, 1,\
        "Hebb", None, [])
    sectionT1B = Section("PHYS 117 T1B", {"Mon": (1400, 1500)}, 1,\
        "Hebb", None, [])
    sectionT1C = Section("PHYS 117 T1C", {"Tue": (1100, 1200)}, 1,\
        "Hebb", None, [])
    sectionT1D = Section("PHYS 117 T1D", {"Tue": (1300, 1400)}, 1,\
        "Hebb", None, [])
    sectionT1E = Section("PHYS 117 T1E", {"Tue": (1530, 1630)}, 1,\
        "Hebb", None, [])
    sectionT1F = Section("PHYS 117 T1F", {"Mon": (1300, 1400)}, 1,\
        "Hebb", None, [])
    sectionT1G = Section("PHYS 117 T1G", {"Mon": (1600, 1700)}, 1,\
        "Hebb", None, [])
    sectionT1N = Section("PHYS 117 T1N", {"Mon": (1500, 1600)}, 1,\
        "Hebb", None, [])
    sectionT1O = Section("PHYS 117 T1O", {"Tue": (1000, 1100)}, 1,\
        "Hebb", None, [])
    
    section101 = Section("PHYS 117 101", {"Mon": (1100, 1200),\
        "Wed": (1100, 1200), "Fri": (1100, 1200)}, 1, "Hebb", "Joss Ives",\
            [sectionT1A, sectionT1B, sectionT1C, sectionT1D, sectionT1E,\
                sectionT1F, sectionT1G, sectionT1N, sectionT1O])
    section102 = Section("PHYS 117 102", {"Mon": (1500, 1600),\
        "Wed": (1500, 1600), "Fri": (1500, 1600)}, 1, "Hennings", "Joss Ives",\
            [sectionT1A, sectionT1B, sectionT1C, sectionT1D, sectionT1E,\
                sectionT1F, sectionT1G, sectionT1N, sectionT1O])
    return [section101, section102]


def getPHYS119Sections() -> list[Section]:
    sectionL1A = Section("PHYS 119 L1A", {"Wed": (1400, 1700)}, 1,\
        "Hebb", "Carl Michal", [])
    sectionL1B = Section("PHYS 119 L1B", {"Thu": (930, 1230)}, 1,\
        "Hebb", "Carl Michal", [])
    sectionL1D = Section("PHYS 119 L1D", {"Wed": (1100, 1400)}, 1,\
        "Hebb", "Carl Michal", [])
    sectionL1F = Section("PHYS 119 L1F", {"Fri": (1400, 1700)}, 1,\
        "Hebb", "Carl Michal", [])

    sectionL2A = Section("PHYS 119 L2A", {"Tue": (800, 1100)}, 2,\
        "Hebb", "Joss Ives", [])
    sectionL2B = Section("PHYS 119 L2B", {"Tue": (1100, 1400)}, 2,\
        "Hebb", "Joss Ives", [])
    sectionL2C = Section("PHYS 119 L2C", {"Tue": (1400, 1700)}, 2,\
        "Hebb", "Alison Lister", [])
    sectionL2D = Section("PHYS 119 L2D", {"Wed": (1100, 1400)}, 2,\
        "Hebb", "Alison Lister", [])
    sectionL2E = Section("PHYS 119 L2E", {"Thu": (1400, 1700)}, 2,\
        "Hebb", "Alison Lister", [])
    sectionL2F = Section("PHYS 119 L2F", {"Fri": (1400, 1700)}, 2,\
        "Hebb", "Alison Lister", [])
    sectionL2G = Section("PHYS 119 L2G", {"Thu": (800, 1100)}, 2,\
        "Hebb", "Alison Lister", [])
    
    return [sectionL1A, sectionL1B, sectionL1D, sectionL1F,\
        sectionL2A, sectionL2B, sectionL2C, sectionL2D, sectionL2E, sectionL2F, sectionL2G]

if __name__ == "__main__":
    math100Sections = getMATH100Sections()
    phys117Sections = getPHYS117Sections()
    phys119Sections = getPHYS119Sections()

    math100 = Course("MATH 100", math100Sections, 3)
    phys117 = Course("PHYS 117", phys117Sections, 3)
    phys119 = Course("PHYS 119", phys119Sections, 1)

    coursesToSchedule = [math100, phys117, phys119]
    scheduler = Scheduler()
    scheduler.schedule(coursesToSchedule)
    timetables = scheduler.getTimetables()

    for timetable in timetables:
        sections = timetable.getSections()
        for section in sections:
            print(f"{section.getSectionName()} : {section.getTime()}")