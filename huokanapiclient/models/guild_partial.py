from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="GuildPartial")


@attr.s(auto_attribs=True)
class GuildPartial:
    """
    Attributes:
        name (str):
        realm (str):
    """

    name: str
    realm: str

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        realm = self.realm

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "realm": realm,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        realm = d.pop("realm")

        guild_partial = cls(
            name=name,
            realm=realm,
        )

        return guild_partial
