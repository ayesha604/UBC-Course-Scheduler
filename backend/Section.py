class Section:
    sectionName = ""
    day = ""
    startTime = 0
    endTime = 0
    term = 1 # 1 or 2
    location = ""
    professor = ""
    dependencies = [] # [Section]

    def __init__(self) -> None:
        pass

    def getSectionName(self) -> str:
        """return section name"""
        pass

    def getTime(self) -> dict[str: tuple(int, int)]:
        """Return a dict with day as key and (start, end) as value""" 
        pass

    def getTerm(self) -> int:
        """return the term the section is offered in"""
        pass

    def getLocation(self) -> str:
        """return the building the section is offered in"""
        pass

    def getProf(self) -> str:
        """return the instructor's name"""
        pass

    def getDependencies(self) -> list[str]:
        """return a list of dependencies (e.g., labs, tutorials, etc.)"""
        pass