import itertools
from backend.objects.Timetable import *
from backend.objects.NewSection import *
from backend.objects.Course import *

class Scheduler:
    timetables = []
    MAX_TIMETABLES = 100000
    EARLIEST_TIME = 800
    LATEST_TIME = 2200
    CUTOFF_TIME = (LATEST_TIME - EARLIEST_TIME) / 2 + EARLIEST_TIME

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
                timetable.setScore(self.calculateScore(timetable))
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

        

    def calculateScore(self, timetable: Timetable) -> int:
        allSections = timetable.getSections()
        schedule = {"Mon": [], "Tue": [],\
            "Wed": [], "Thu": [], "Fri": []}
        for section in allSections:
            for d in section.times.keys():
                schedule[d].append(section.times[d])
        
        score = 0
        maxScoreFromNumClass = 50
        maxScoreFromSpacedClass = 8
        maxScoreFromLateTime = self.spaceBetweenTime(self.LATEST_TIME, self.CUTOFF_TIME)
        for d in schedule.keys():
            if len(schedule[d]) == 0: # prep-day
                score += maxScoreFromNumClass
                continue
            # award less for more classes
            score += int(maxScoreFromNumClass/len(schedule[d]))

            schedule[d].sort()
            earliestClass = schedule[d][0]
            latestClass = schedule[d][-1]
            if earliestClass[0] <= self.CUTOFF_TIME: # bonus for starting late
                score += self.spaceBetweenTime(earliestClass[0], self.EARLIEST_TIME)
            else: # penalize for starting too late
                score -= self.spaceBetweenTime(earliestClass[0], self.CUTOFF_TIME)

            score += max(self.spaceBetweenTime(self.LATEST_TIME, latestClass[1]),\
                maxScoreFromSpacedClass) # bonus for ending early
            
            for i in range(len(schedule[d]) - 1): # bonus for spaced class
                currClass = schedule[d][i]
                nextClass = schedule[d][i + 1]
                score += max(self.spaceBetweenTime(nextClass[0], currClass[1]),\
                    maxScoreFromSpacedClass)

        return score


    def spaceBetweenTime(self, slotOne: int, slotTwo: int) -> int:
        """Return space between two time in units of 30 minutes"""
        return int((slotOne - slotTwo)/100) + (slotOne - slotTwo) % 100 / 70


    def rankTimetables(self) -> None:
        """rank the timeTables based on score (in place)"""
        pass

    def getTimetables(self) -> list[Timetable]:
        """return the possible timetables (in order)"""
        return self.timetables.copy()