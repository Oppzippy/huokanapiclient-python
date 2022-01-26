import datetime
from typing import Any, Dict, Type, TypeVar

import attr
from dateutil.parser import isoparse

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
        approximate_deposit_timestamp (datetime.datetime):
    """

    id: str
    endorsements: int
    character_name: str
    character_realm: str
    deposit_in_copper: int
    approximate_deposit_timestamp: datetime.datetime

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        endorsements = self.endorsements
        character_name = self.character_name
        character_realm = self.character_realm
        deposit_in_copper = self.deposit_in_copper
        approximate_deposit_timestamp = self.approximate_deposit_timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "endorsements": endorsements,
                "characterName": character_name,
                "characterRealm": character_realm,
                "depositInCopper": deposit_in_copper,
                "approximateDepositTimestamp": approximate_deposit_timestamp,
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

        approximate_deposit_timestamp = isoparse(d.pop("approximateDepositTimestamp"))

        deposit = cls(
            id=id,
            endorsements=endorsements,
            character_name=character_name,
            character_realm=character_realm,
            deposit_in_copper=deposit_in_copper,
            approximate_deposit_timestamp=approximate_deposit_timestamp,
        )

        return deposit
