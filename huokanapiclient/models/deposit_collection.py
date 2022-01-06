from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.deposit import Deposit

T = TypeVar("T", bound="DepositCollection")


@attr.s(auto_attribs=True)
class DepositCollection:
    """
    Attributes:
        deposits (List[Deposit]):
    """

    deposits: List[Deposit]

    def to_dict(self) -> Dict[str, Any]:
        deposits = []
        for deposits_item_data in self.deposits:
            deposits_item = deposits_item_data.to_dict()

            deposits.append(deposits_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "deposits": deposits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        deposits = []
        _deposits = d.pop("deposits")
        for deposits_item_data in _deposits:
            deposits_item = Deposit.from_dict(deposits_item_data)

            deposits.append(deposits_item)

        deposit_collection = cls(
            deposits=deposits,
        )

        return deposit_collection
