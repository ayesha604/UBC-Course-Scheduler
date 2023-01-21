from Section import *

class Course:
    sections = {} # {"name": Section}
    creditsNum = 0

    def __init__(self) -> None:
        pass

    def addSection(self, section: Section) -> None:
        """Add a (lecture) section the list of Sections"""
        pass

    def getSections(self) -> list[Section]:
        """return a list of all Sections offered for this course"""
        pass 
    
    def getCredits(self) -> None:
        """return the credits of the course"""
        pass