import itertools
import random
from backend.objects.Timetable import *
from backend.objects.Section import *
from backend.objects.Course import *

class Scheduler:
    MAX_TIMETABLES = 5000
    SUB_MAX_TIMETABLES = MAX_TIMETABLES / 100
    EARLIEST_TIME = 800
    LATEST_TIME = 2200
    CUTOFF_TIME = (LATEST_TIME - EARLIEST_TIME) / 2 + EARLIEST_TIME

    def __init__(self):
        self.timetables = []

    def schedule(self, inputCourses: list[Course], term: int) -> None:
        """create all possible timetables from the given courses (in order)"""
        memo = []
        def dfs(inputCourses: list[Course], timetable: Timetable, targetSize: int) -> None:
            if len(self.timetables) == targetSize:
                return
            if len(inputCourses) == 0:
                sectionNamesInTimeTable = timetable.getSectionNames()
                if sectionNamesInTimeTable not in memo:
                    timetable.setScore(self.calculateScore(timetable))
                    self.timetables.append(timetable)
                    memo.append(sectionNamesInTimeTable)
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
                        random.shuffle(allCombinations)
                        if len(allCombinations) != 0:
                            for comb in allCombinations:
                                tempTimetable = Timetable(newTimetable.getSections())
                                isSuccessful = True
                                for s in comb:
                                    if not tempTimetable.addSection(s):
                                        isSuccessful = False
                                        break
                                if isSuccessful:
                                    dfs(inputCourses[1:], tempTimetable, targetSize)
                        else:
                            dfs(inputCourses[1:], newTimetable, targetSize)
        currTargetSize = self.SUB_MAX_TIMETABLES

        while currTargetSize != self.MAX_TIMETABLES:
            dfs(inputCourses, Timetable([], 0), currTargetSize)
            currTargetSize += self.SUB_MAX_TIMETABLES
        self.rankTimetables()

    def calculateScore(self, timetable: Timetable) -> int:
        """Calculate the score for a timetable based on:
            + number of classes in a day
            + start-time and end-time
            + space in between classes
            + lunch-break"""
        allSections = timetable.getSections()
        schedule = {"Mon": [], "Tue": [],\
            "Wed": [], "Thu": [], "Fri": []}
        for section in allSections:
            for d in section.times.keys():
                schedule[d].append(section.times[d])
        
        score = 0
        maxScoreFromNumClass = 8
        maxScoreFromSpacedClass = 8
        idealEndTime = 1600
        maxScoreFromLateTime = 5
        idealStartTime = 1000
        maxScoreFromEarlyTime = 6 # 2 would be the latest
        lunchBreak = (1100, 1300)
        scoreForLunchBreak = 5
        for d in schedule.keys():
            if len(schedule[d]) == 0: # prep-day
                score += maxScoreFromNumClass
                continue
            # award less for more classes
            score += int(maxScoreFromNumClass/(len(schedule[d]) + 1))

            schedule[d].sort(key=lambda t: t[0])
            earliestClass = schedule[d][0]
            latestClass = schedule[d][-1]
            if earliestClass[0] >= idealStartTime:
                score += min(self.spaceBetweenTime(earliestClass[0], idealStartTime),\
                    maxScoreFromEarlyTime)
            else: # penalize for starting too early
                score -= self.spaceBetweenTime(idealEndTime, earliestClass[0])

            if latestClass[1] <= idealEndTime: # penalize for ending too late
                score += min(self.spaceBetweenTime(latestClass[0], idealEndTime), maxScoreFromLateTime)
            else:
                score -= self.spaceBetweenTime(latestClass[1], idealEndTime) * 2
            
            hasLunchBreak = True
            for i in range(len(schedule[d]) - 1): # bonus for spaced class
                currClass = schedule[d][i]
                nextClass = schedule[d][i + 1]
                score += min(self.spaceBetweenTime(nextClass[0], currClass[1]),\
                    maxScoreFromSpacedClass)
                if currClass[0] >= lunchBreak[0] and currClass[1] <= lunchBreak[1]:
                    hasLunchBreak = False
            score += scoreForLunchBreak if hasLunchBreak else 0 

        return max(score,0)

    def spaceBetweenTime(self, slotOne: int, slotTwo: int) -> int:
        """Return space between two time in units of 30 minutes"""
        difference = slotOne - slotTwo
        extra = 1 if difference % 100 != 0 else 0
        return int(difference/100) + extra

    def rankTimetables(self) -> None:
        """rank the timeTables based on score (in place)"""
        self.timetables.sort(key=lambda t: t.getScore(), reverse=True)
        

    def getTimetables(self) -> list[Timetable]:
        """return the possible timetables (in order)"""
        return self.timetables.copy()

    def getTopTimetables(self, top=3) -> list[Timetable]:
        if top >= len(self.timetables): 
            return self.timetables.copy()
        
        return self.timetables[0:top]

    def getWorstTimetables(self, worst=3) -> list[Timetable]:
        if worst >= len(self.timetables):
            return self.timetables.copy()
        return self.timetables[-worst:]

    def to_dict(self, num_tables: int) -> dict:
        """Return a dict formatted in the same way as timetable.json"""
        timetables_list = [t.to_dict() for t in self.getTopTimetables(num_tables)]
        return {"timetables": timetables_list}
