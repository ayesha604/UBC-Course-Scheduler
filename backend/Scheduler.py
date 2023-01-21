from Timetable import *
from Section import *
from Course import *

class Scheduler:
    timetables = []

    def __init__(self) -> None:
        """create a scheduler"""
        return

    def schedule(self, inputCourses: list[Course]) -> list[Timetable]:
        """create all possible timetables from the given courses (in order)"""
        pass

    def calculateScore(self, timeTable: Timetable) -> int:
        pass

    def rankTimetables(self) -> None:
        """rank the timeTables based on score (in place)"""
        pass

    def getTimetables(self) -> list[Timetable]:
        """return the possible timetables (in order)"""
        return self.timetables.copy()