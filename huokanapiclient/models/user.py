from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        id (str):
        discord_user_id (str):
    """

    id: str
    discord_user_id: str

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        discord_user_id = self.discord_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "discordUserId": discord_user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        discord_user_id = d.pop("discordUserId")

        user = cls(
            id=id,
            discord_user_id=discord_user_id,
        )

        return user
