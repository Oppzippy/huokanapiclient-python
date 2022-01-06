from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="Authorization")


@attr.s(auto_attribs=True)
class Authorization:
    """
    Attributes:
        api_key (str):
    """

    api_key: str

    def to_dict(self) -> Dict[str, Any]:
        api_key = self.api_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "apiKey": api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_key = d.pop("apiKey")

        authorization = cls(
            api_key=api_key,
        )

        return authorization
