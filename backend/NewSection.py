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



