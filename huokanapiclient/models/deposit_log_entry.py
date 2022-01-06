from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="DepositLogEntry")


@attr.s(auto_attribs=True)
class DepositLogEntry:
    """
    Attributes:
        character_name (str):
        character_realm (str):
        deposit_in_copper (int):
        guild_bank_copper (int):
    """

    character_name: str
    character_realm: str
    deposit_in_copper: int
    guild_bank_copper: int

    def to_dict(self) -> Dict[str, Any]:
        character_name = self.character_name
        character_realm = self.character_realm
        deposit_in_copper = self.deposit_in_copper
        guild_bank_copper = self.guild_bank_copper

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "characterName": character_name,
                "characterRealm": character_realm,
                "depositInCopper": deposit_in_copper,
                "guildBankCopper": guild_bank_copper,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        character_name = d.pop("characterName")

        character_realm = d.pop("characterRealm")

        deposit_in_copper = d.pop("depositInCopper")

        guild_bank_copper = d.pop("guildBankCopper")

        deposit_log_entry = cls(
            character_name=character_name,
            character_realm=character_realm,
            deposit_in_copper=deposit_in_copper,
            guild_bank_copper=guild_bank_copper,
        )

        return deposit_log_entry
