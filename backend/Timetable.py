from Section import *

class Timetable:
    sections = []
    score = 0

    def __init__(self, sections: list[Section], score: int) -> None:
        """create a timetable with a given score"""
        self.sections = sections
        self.score = score
        return

    def getScore(self) -> int:
        """return the score for the timetable"""
        return self.score

    def getSections(self) -> None:
        """return a list of all sections in the timetable"""
        return self.sections.copy()