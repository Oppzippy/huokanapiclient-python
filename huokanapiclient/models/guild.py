from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="Guild")


@attr.s(auto_attribs=True)
class Guild:
    """
    Attributes:
        name (str):
        realm (str):
        id (str):
    """

    name: str
    realm: str
    id: str

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        realm = self.realm
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "realm": realm,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        realm = d.pop("realm")

        id = d.pop("id")

        guild = cls(
            name=name,
            realm=realm,
            id=id,
        )

        return guild
