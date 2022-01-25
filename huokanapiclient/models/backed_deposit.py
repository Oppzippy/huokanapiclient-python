from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackedDeposit")


@attr.s(auto_attribs=True)
class BackedDeposit:
    """
    Attributes:
        id (Union[Unset, str]):
        endorsements (Union[Unset, int]):
        character_name (Union[Unset, None, str]):
        character_realm (Union[Unset, None, str]):
        deposit_in_copper (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    endorsements: Union[Unset, int] = UNSET
    character_name: Union[Unset, None, str] = UNSET
    character_realm: Union[Unset, None, str] = UNSET
    deposit_in_copper: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        endorsements = self.endorsements
        character_name = self.character_name
        character_realm = self.character_realm
        deposit_in_copper = self.deposit_in_copper

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if endorsements is not UNSET:
            field_dict["endorsements"] = endorsements
        if character_name is not UNSET:
            field_dict["characterName"] = character_name
        if character_realm is not UNSET:
            field_dict["characterRealm"] = character_realm
        if deposit_in_copper is not UNSET:
            field_dict["depositInCopper"] = deposit_in_copper

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        endorsements = d.pop("endorsements", UNSET)

        character_name = d.pop("characterName", UNSET)

        character_realm = d.pop("characterRealm", UNSET)

        deposit_in_copper = d.pop("depositInCopper", UNSET)

        backed_deposit = cls(
            id=id,
            endorsements=endorsements,
            character_name=character_name,
            character_realm=character_realm,
            deposit_in_copper=deposit_in_copper,
        )

        return backed_deposit
