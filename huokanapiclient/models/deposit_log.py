import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.deposit_log_entry import DepositLogEntry

T = TypeVar("T", bound="DepositLog")


@attr.s(auto_attribs=True)
class DepositLog:
    """
    Attributes:
        log (List[DepositLogEntry]):
        captured_at (datetime.datetime):
    """

    log: List[DepositLogEntry]
    captured_at: datetime.datetime

    def to_dict(self) -> Dict[str, Any]:
        log = []
        for log_item_data in self.log:
            log_item = log_item_data.to_dict()

            log.append(log_item)

        captured_at = self.captured_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "log": log,
                "capturedAt": captured_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        log = []
        _log = d.pop("log")
        for log_item_data in _log:
            log_item = DepositLogEntry.from_dict(log_item_data)

            log.append(log_item)

        captured_at = isoparse(d.pop("capturedAt"))

        deposit_log = cls(
            log=log,
            captured_at=captured_at,
        )

        return deposit_log
