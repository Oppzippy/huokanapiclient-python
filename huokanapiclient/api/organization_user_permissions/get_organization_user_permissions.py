from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.organization_permission_collection import OrganizationPermissionCollection
from ...types import Response


def _get_kwargs(
    organization_id: str,
    user_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/organizations/{organizationId}/users/{userId}/permissions".format(
        client.base_url, organizationId=organization_id, userId=user_id
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[OrganizationPermissionCollection]:
    if response.status_code == 200:
        response_200 = OrganizationPermissionCollection.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[OrganizationPermissionCollection]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    organization_id: str,
    user_id: str,
    *,
    client: Client,
) -> Response[OrganizationPermissionCollection]:
    """
    Args:
        organization_id (str):
        user_id (str):

    Returns:
        Response[OrganizationPermissionCollection]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        user_id=user_id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    organization_id: str,
    user_id: str,
    *,
    client: Client,
) -> Optional[OrganizationPermissionCollection]:
    """
    Args:
        organization_id (str):
        user_id (str):

    Returns:
        Response[OrganizationPermissionCollection]
    """

    return sync_detailed(
        organization_id=organization_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    user_id: str,
    *,
    client: Client,
) -> Response[OrganizationPermissionCollection]:
    """
    Args:
        organization_id (str):
        user_id (str):

    Returns:
        Response[OrganizationPermissionCollection]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    organization_id: str,
    user_id: str,
    *,
    client: Client,
) -> Optional[OrganizationPermissionCollection]:
    """
    Args:
        organization_id (str):
        user_id (str):

    Returns:
        Response[OrganizationPermissionCollection]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
