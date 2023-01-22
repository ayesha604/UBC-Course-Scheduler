from typing import TypeVar
T = TypeVar('T', bound="Section")

class Section:
    sectionName = ""
    time = {} # {"day": (startTime, endTime)}
    term = 1 # 1 or 2
    location = ""
    professor = ""
    dependencies = [] # [Section]
    sectionType = ""
    requirements = []
    status = ""

    def __init__(self, sectionName:str, time: dict[str : tuple[int, int]],\
        term: int, location: str, professor: str, dependencies: list[T],\
            sectionType: str, requires: list[str], status: str) -> None:
        """Create a section with all the necessary information"""
        self.sectionName = sectionName
        self.time = time
        self.term = term
        self.location = location
        self.professor = professor
        self.dependencies = dependencies
        self.sectionType = sectionType
        self.requirements = requires
        self.status = status
        return


    def getSectionName(self) -> str:
        """return section name"""
        return self.sectionName

    def getTime(self) -> dict[str: tuple[int, int]]:
        """Return a dict with day as key and (start, end) as value""" 
        return self.time.copy()

    def getTerm(self) -> int:
        """return the term the section is offered in"""
        return self.term

    def getLocation(self) -> str:
        """return the building the section is offered in"""
        return self.location

    def getProf(self) -> str:
        """return the instructor's name"""
        return self.professor

    def getDependencies(self) -> list[T]:
        """return a list of dependencies (e.g., labs, tutorials, etc.)"""
        return self.dependencies.copy()
    
    def getRequirements(self) -> list[str]:
        return self.requirements.copy()
    
    def getSectionType(self) -> str:
        return self.sectionType