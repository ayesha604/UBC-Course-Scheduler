import itertools
from backend.objects.Timetable import *
from backend.objects.Section import *
from backend.objects.Course import *

class Scheduler:
    timetables = []
    MAX_TIMETABLES = 100000

    def __init__(self) -> None:
        """create a scheduler"""
        return

    def schedule(self, inputCourses: list[Course], term: int) -> None:
        """create all possible timetables from the given courses (in order)"""
        def dfs(inputCourses: list[Course], timetable: Timetable) -> None:
            if len(self.timetables) == self.MAX_TIMETABLES:
                return
            if len(inputCourses) == 0:
                # print(len(self.timeTables))
                self.timetables.append(timetable)
            else:
                currCourse = inputCourses[0]
                allSections = currCourse.getSections()
                for section in allSections:
                    if section.term != term:
                        continue
                    newTimetable = Timetable(timetable.getSections())
                    
                    if newTimetable.addSection(section):
                        dependencies = []
                        for r in currCourse.getRequirements():
                            dependencies.append(list(filter(lambda d: d.activity == r and d.term == term, section.dependencies)))
                         
                        allCombinations = list(itertools.product(*dependencies))

                        if len(allCombinations) != 0:
                            for comb in allCombinations:
                                tempTimetable = Timetable(newTimetable.getSections())
                                for s in comb:
                                    if not tempTimetable.addSection(s):
                                        continue
                                dfs(inputCourses[1:], tempTimetable)
                        else:
                            dfs(inputCourses[1:], newTimetable)
        
        dfs(inputCourses, Timetable([], 0))

        

    def calculateScore(self, timeTable: Timetable) -> int:
        pass

    def rankTimetables(self) -> None:
        """rank the timeTables based on score (in place)"""
        pass

    def getTimetables(self) -> list[Timetable]:
        """return the possible timetables (in order)"""
        return self.timetables.copy()