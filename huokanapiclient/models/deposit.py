from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="Deposit")


@attr.s(auto_attribs=True)
class Deposit:
    """
    Attributes:
        id (str):
        endorsements (int):
        character_name (str):
        character_realm (str):
        deposit_in_copper (int):
    """

    id: str
    endorsements: int
    character_name: str
    character_realm: str
    deposit_in_copper: int

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        endorsements = self.endorsements
        character_name = self.character_name
        character_realm = self.character_realm
        deposit_in_copper = self.deposit_in_copper

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "endorsements": endorsements,
                "characterName": character_name,
                "characterRealm": character_realm,
                "depositInCopper": deposit_in_copper,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        endorsements = d.pop("endorsements")

        character_name = d.pop("characterName")

        character_realm = d.pop("characterRealm")

        deposit_in_copper = d.pop("depositInCopper")

        deposit = cls(
            id=id,
            endorsements=endorsements,
            character_name=character_name,
            character_realm=character_realm,
            deposit_in_copper=deposit_in_copper,
        )

        return deposit
