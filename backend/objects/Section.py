import dataclasses
import json
from dataclasses import dataclass
from typing import TypeVar

T = TypeVar('T', bound="Section")


@dataclass
class Section:
    status: str
    name: str
    activity: str
    term: int
    mode: str
    times: dict[str: tuple[int, int]]

    location: str = None
    professor: str = None
    dependencies: list[T] = None

    def to_dict(self) -> dict:
        """Returns dict formatted the same way as timetable.json"""
        days = []
        for day in self.times.keys():
            start_time, end_time = self.times[day]
            start_time = str(start_time)
            start_time = start_time[:-2] + ":" + start_time[-2:]
            end_time = str(end_time)
            end_time = end_time[:-2] + ":" + end_time[-2:]
            days.append({"day": day,
                         "times": [start_time, end_time]})
        return {"section": {"name": self.name,
                            "days": days,
                            "location": self.location,
                            "professors": [self.professor],
                            "status": self.status}}
