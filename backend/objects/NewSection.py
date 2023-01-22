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

    def to_json(self) -> str:
        return json.dumps(dataclasses.asdict(self))
