from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.guild_collection import GuildCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    realm: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/organizations/{organizationId}/guilds".format(client.base_url, organizationId=organization_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "name": name,
        "realm": realm,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[GuildCollection]:
    if response.status_code == 200:
        response_200 = GuildCollection.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GuildCollection]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    organization_id: str,
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    realm: Union[Unset, None, str] = UNSET,
) -> Response[GuildCollection]:
    """
    Args:
        organization_id (str):
        name (Union[Unset, None, str]):
        realm (Union[Unset, None, str]):

    Returns:
        Response[GuildCollection]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        client=client,
        name=name,
        realm=realm,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    organization_id: str,
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    realm: Union[Unset, None, str] = UNSET,
) -> Optional[GuildCollection]:
    """
    Args:
        organization_id (str):
        name (Union[Unset, None, str]):
        realm (Union[Unset, None, str]):

    Returns:
        Response[GuildCollection]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        name=name,
        realm=realm,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    realm: Union[Unset, None, str] = UNSET,
) -> Response[GuildCollection]:
    """
    Args:
        organization_id (str):
        name (Union[Unset, None, str]):
        realm (Union[Unset, None, str]):

    Returns:
        Response[GuildCollection]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        client=client,
        name=name,
        realm=realm,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    realm: Union[Unset, None, str] = UNSET,
) -> Optional[GuildCollection]:
    """
    Args:
        organization_id (str):
        name (Union[Unset, None, str]):
        realm (Union[Unset, None, str]):

    Returns:
        Response[GuildCollection]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            name=name,
            realm=realm,
        )
    ).parsed
