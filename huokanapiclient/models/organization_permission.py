from enum import Enum


class OrganizationPermission(str, Enum):
    ADMINISTRATOR = "ADMINISTRATOR"
    MODERATOR = "MODERATOR"
    MEMBER = "MEMBER"

    def __str__(self) -> str:
        return str(self.value)
