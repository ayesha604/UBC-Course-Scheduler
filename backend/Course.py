from backend.Section import *

class Course:
    courseName = ""
    sections = [] # [Section]
    creditsNum = 0

    def __init__(self, courseName: str, sections: list[Section], requirements: list[str], creditsNum: int) -> None:
        """Create a course object"""
        self.courseName = courseName
        self.sections = sections
        self.creditsNum = creditsNum
        self.requirements = requirements
        return

    def __str__(self):
        return f'name={self.courseName}, requirements={self.requirements} sections={self.sections}'

    def getSections(self) -> list[Section]:
        """return a list of all Sections offered for this course"""
        return self.sections.copy()
    
    def getCredits(self) -> int:
        """return the credits of the course"""
        return self.creditsNum

    def getCourseName(self) -> str:
        """return the course name"""
        return self.courseName

    def getRequirements(self) -> list[str]:
        return self.requirements.copy()
