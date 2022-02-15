from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.deposit_collection import DepositCollection
from ...models.direction import Direction
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    guild_id: str,
    *,
    client: Client,
    direction: Direction,
    relative_to: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
) -> Dict[str, Any]:
    url = "{}/organizations/{organizationId}/guilds/{guildId}/deposits".format(
        client.base_url, organizationId=organization_id, guildId=guild_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_direction = direction.value

    params["direction"] = json_direction

    params["relativeTo"] = relative_to

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[DepositCollection]:
    if response.status_code == 200:
        response_200 = DepositCollection.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[DepositCollection]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    organization_id: str,
    guild_id: str,
    *,
    client: Client,
    direction: Direction,
    relative_to: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
) -> Response[DepositCollection]:
    """
    Args:
        organization_id (str):
        guild_id (str):
        direction (Direction):
        relative_to (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 50.

    Returns:
        Response[DepositCollection]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        guild_id=guild_id,
        client=client,
        direction=direction,
        relative_to=relative_to,
        limit=limit,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    organization_id: str,
    guild_id: str,
    *,
    client: Client,
    direction: Direction,
    relative_to: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
) -> Optional[DepositCollection]:
    """
    Args:
        organization_id (str):
        guild_id (str):
        direction (Direction):
        relative_to (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 50.

    Returns:
        Response[DepositCollection]
    """

    return sync_detailed(
        organization_id=organization_id,
        guild_id=guild_id,
        client=client,
        direction=direction,
        relative_to=relative_to,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    guild_id: str,
    *,
    client: Client,
    direction: Direction,
    relative_to: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
) -> Response[DepositCollection]:
    """
    Args:
        organization_id (str):
        guild_id (str):
        direction (Direction):
        relative_to (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 50.

    Returns:
        Response[DepositCollection]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        guild_id=guild_id,
        client=client,
        direction=direction,
        relative_to=relative_to,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    organization_id: str,
    guild_id: str,
    *,
    client: Client,
    direction: Direction,
    relative_to: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
) -> Optional[DepositCollection]:
    """
    Args:
        organization_id (str):
        guild_id (str):
        direction (Direction):
        relative_to (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 50.

    Returns:
        Response[DepositCollection]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            guild_id=guild_id,
            client=client,
            direction=direction,
            relative_to=relative_to,
            limit=limit,
        )
    ).parsed
