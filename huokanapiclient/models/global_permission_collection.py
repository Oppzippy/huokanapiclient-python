from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.global_permission import GlobalPermission

T = TypeVar("T", bound="GlobalPermissionCollection")


@attr.s(auto_attribs=True)
class GlobalPermissionCollection:
    """
    Attributes:
        permissions (List[GlobalPermission]):
    """

    permissions: List[GlobalPermission]

    def to_dict(self) -> Dict[str, Any]:
        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.value

            permissions.append(permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "permissions": permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = GlobalPermission(permissions_item_data)

            permissions.append(permissions_item)

        global_permission_collection = cls(
            permissions=permissions,
        )

        return global_permission_collection
