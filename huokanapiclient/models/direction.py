from enum import Enum


class Direction(str, Enum):
    NEWER = "NEWER"
    OLDER = "OLDER"

    def __str__(self) -> str:
        return str(self.value)
