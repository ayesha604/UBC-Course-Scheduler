from Section import *

class Course:
    courseName = ""
    sections = [] # [Section]
    creditsNum = 0

    def __init__(self, courseName: str) -> None:
        """Create a course object"""
        pass

    def addSection(self, section: Section) -> None:
        """Add a (lecture) section the list of Sections"""
        pass

    def getSections(self) -> list[Section]:
        """return a list of all Sections offered for this course"""
        pass 
    
    def getCredits(self) -> int:
        """return the credits of the course"""
        pass

    def getCourseName(self) -> str:
        """return the course name"""
        pass