from enum import Enum


class GlobalPermission(str, Enum):
    ADMINISTRATOR = "ADMINISTRATOR"

    def __str__(self) -> str:
        return str(self.value)
