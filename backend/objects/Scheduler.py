import itertools
import random
from backend.objects.Timetable import *
from backend.objects.Section import *
from backend.objects.Course import *

class Scheduler:
    timetables = []
    MAX_TIMETABLES = 10_000
    SUB_MAX_TIMETABLES = MAX_TIMETABLES / 1000
    EARLIEST_TIME = 800
    LATEST_TIME = 2200
    CUTOFF_TIME = (LATEST_TIME - EARLIEST_TIME) / 2 + EARLIEST_TIME

    def __init__(self) -> None:
        """create a scheduler"""
        return

    def schedule(self, inputCourses: list[Course], term: int) -> None:
        """create all possible timetables from the given courses (in order)"""
        def dfs(inputCourses: list[Course], timetable: Timetable) -> None:
            if len(self.timetables) % self.SUB_MAX_TIMETABLES == 0:
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
                                    dfs(inputCourses[1:], tempTimetable)
                        else:
                            dfs(inputCourses[1:], newTimetable)
        while len(self.timetables) != self.MAX_TIMETABLES: 
            dfs(inputCourses, Timetable([], 0))
        print('aa')
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
        maxScoreFromNumClass = 5
        maxScoreFromSpacedClass = 8
        idealEndTime = 1600
        maxScoreFromLateTime = 5
        idealStartTime = 1000
        maxScoreFromEarlyTime = 4 # 2 would be the latest
        lunchBreak = (1100, 1300)
        scoreForLunchBreak = 5
        for d in schedule.keys():
            if len(schedule[d]) == 0: # prep-day
                score += maxScoreFromNumClass
                continue
            # award less for more classes
            # score += int(maxScoreFromNumClass/(len(schedule[d]) + 1))

            schedule[d].sort(key=lambda t: t[0])
            earliestClass = schedule[d][0]
            latestClass = schedule[d][-1]
            # if earliestClass[0] <= self.CUTOFF_TIME: # bonus for starting late
            #     score += self.spaceBetweenTime(earliestClass[0], self.EARLIEST_TIME)
            # else: # penalize for starting too late
            #     score -= self.spaceBetweenTime(earliestClass[0], self.CUTOFF_TIME) * 5
            if earliestClass[0] >= idealStartTime:
                score += min(self.spaceBetweenTime(earliestClass[0], idealStartTime),\
                    maxScoreFromEarlyTime)
            else: # penalize for starting too early
                score -= self.spaceBetweenTime(idealEndTime, earliestClass[0])

            if latestClass[1] <= idealEndTime: # penalize for ending too late
                score += min(self.spaceBetweenTime(latestClass[0], idealEndTime), maxScoreFromLateTime)
            else:
                score -= self.spaceBetweenTime(latestClass[1], idealEndTime)
            
            hasLunchBreak = True
            for i in range(len(schedule[d]) - 1): # bonus for spaced class
                currClass = schedule[d][i]
                nextClass = schedule[d][i + 1]
                score += min(self.spaceBetweenTime(nextClass[0], currClass[1]),\
                    maxScoreFromSpacedClass)
                if currClass[0] >= lunchBreak[0] and currClass[1] <= lunchBreak[1]:
                    hasLunchBreak = False
            score += scoreForLunchBreak if hasLunchBreak else 0 

        return score


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