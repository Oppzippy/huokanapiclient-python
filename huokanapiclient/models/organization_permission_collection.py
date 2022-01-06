from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.organization_permission import OrganizationPermission

T = TypeVar("T", bound="OrganizationPermissionCollection")


@attr.s(auto_attribs=True)
class OrganizationPermissionCollection:
    """
    Attributes:
        permissions (List[OrganizationPermission]):
    """

    permissions: List[OrganizationPermission]

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
            permissions_item = OrganizationPermission(permissions_item_data)

            permissions.append(permissions_item)

        organization_permission_collection = cls(
            permissions=permissions,
        )

        return organization_permission_collection
