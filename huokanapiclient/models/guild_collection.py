from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.guild import Guild

T = TypeVar("T", bound="GuildCollection")


@attr.s(auto_attribs=True)
class GuildCollection:
    """
    Attributes:
        guilds (List[Guild]):
    """

    guilds: List[Guild]

    def to_dict(self) -> Dict[str, Any]:
        guilds = []
        for guilds_item_data in self.guilds:
            guilds_item = guilds_item_data.to_dict()

            guilds.append(guilds_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "guilds": guilds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guilds = []
        _guilds = d.pop("guilds")
        for guilds_item_data in _guilds:
            guilds_item = Guild.from_dict(guilds_item_data)

            guilds.append(guilds_item)

        guild_collection = cls(
            guilds=guilds,
        )

        return guild_collection
