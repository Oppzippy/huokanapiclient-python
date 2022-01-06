from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="OrganizationPartial")


@attr.s(auto_attribs=True)
class OrganizationPartial:
    """
    Attributes:
        name (str):
        slug (str):
        discord_guild_id (str):
    """

    name: str
    slug: str
    discord_guild_id: str

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        slug = self.slug
        discord_guild_id = self.discord_guild_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "discordGuildId": discord_guild_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        slug = d.pop("slug")

        discord_guild_id = d.pop("discordGuildId")

        organization_partial = cls(
            name=name,
            slug=slug,
            discord_guild_id=discord_guild_id,
        )

        return organization_partial
