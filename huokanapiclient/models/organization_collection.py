from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.organization import Organization

T = TypeVar("T", bound="OrganizationCollection")


@attr.s(auto_attribs=True)
class OrganizationCollection:
    """
    Attributes:
        organizations (List[Organization]):
    """

    organizations: List[Organization]

    def to_dict(self) -> Dict[str, Any]:
        organizations = []
        for organizations_item_data in self.organizations:
            organizations_item = organizations_item_data.to_dict()

            organizations.append(organizations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "organizations": organizations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        organizations = []
        _organizations = d.pop("organizations")
        for organizations_item_data in _organizations:
            organizations_item = Organization.from_dict(organizations_item_data)

            organizations.append(organizations_item)

        organization_collection = cls(
            organizations=organizations,
        )

        return organization_collection
