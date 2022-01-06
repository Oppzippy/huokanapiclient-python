import datetime
from typing import Any, Dict, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="Organization")


@attr.s(auto_attribs=True)
class Organization:
    """
    Attributes:
        name (str):
        slug (str):
        discord_guild_id (str):
        id (str):
        created_at (datetime.datetime):
    """

    name: str
    slug: str
    discord_guild_id: str
    id: str
    created_at: datetime.datetime

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        slug = self.slug
        discord_guild_id = self.discord_guild_id
        id = self.id
        created_at = self.created_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "discordGuildId": discord_guild_id,
                "id": id,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        slug = d.pop("slug")

        discord_guild_id = d.pop("discordGuildId")

        id = d.pop("id")

        created_at = isoparse(d.pop("createdAt"))

        organization = cls(
            name=name,
            slug=slug,
            discord_guild_id=discord_guild_id,
            id=id,
            created_at=created_at,
        )

        return organization
