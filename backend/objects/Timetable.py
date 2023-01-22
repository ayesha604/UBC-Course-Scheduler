from objects.Section import *
from objects.NewSection import *

class Timetable:
    sections = []
    score = 0

    def __init__(self, sections: list[Section], score=0) -> None:
        """create a timetable with a given score"""
        self.sections = sections
        self.score = score
        return

    def setScore(self, newScore: int) -> None:
        self.score = newScore

    def addSection(self, newSection: Section) -> bool:
        """Add section to the timetable. Return true if added sucessfully, false otherwise"""
        newSectionTime = newSection.times
        for section in self.sections:
            currSectionTime = section.times
            for day in currSectionTime.keys():
                newTime = newSectionTime.get(day)
                currTime = currSectionTime.get(day)
                if newTime is not None and \
                    not ((newTime[1] <= currTime[0]) or (newTime[0] >= currTime[1])):
                    return False

        self.sections.append(newSection)
        return True

    def getScore(self) -> int:
        """return the score for the timetable"""
        return self.score

    def getSections(self) -> None:
        """return a list of all sections in the timetable"""
        return self.sections.copy()