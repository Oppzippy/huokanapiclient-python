from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.backed_deposit import BackedDeposit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    guild_id: str,
    deposit_id: str,
    *,
    client: Client,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/organizations/{organizationId}/guilds/{guildId}/deposits/{depositId}".format(
        client.base_url, organizationId=organization_id, guildId=guild_id, depositId=deposit_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[BackedDeposit]:
    if response.status_code == 200:
        response_200 = BackedDeposit.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[BackedDeposit]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    organization_id: str,
    guild_id: str,
    deposit_id: str,
    *,
    client: Client,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[BackedDeposit]:
    """
    Args:
        organization_id (str):
        guild_id (str):
        deposit_id (str):
        offset (Union[Unset, None, int]):

    Returns:
        Response[BackedDeposit]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        guild_id=guild_id,
        deposit_id=deposit_id,
        client=client,
        offset=offset,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    organization_id: str,
    guild_id: str,
    deposit_id: str,
    *,
    client: Client,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[BackedDeposit]:
    """
    Args:
        organization_id (str):
        guild_id (str):
        deposit_id (str):
        offset (Union[Unset, None, int]):

    Returns:
        Response[BackedDeposit]
    """

    return sync_detailed(
        organization_id=organization_id,
        guild_id=guild_id,
        deposit_id=deposit_id,
        client=client,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    guild_id: str,
    deposit_id: str,
    *,
    client: Client,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[BackedDeposit]:
    """
    Args:
        organization_id (str):
        guild_id (str):
        deposit_id (str):
        offset (Union[Unset, None, int]):

    Returns:
        Response[BackedDeposit]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        guild_id=guild_id,
        deposit_id=deposit_id,
        client=client,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    organization_id: str,
    guild_id: str,
    deposit_id: str,
    *,
    client: Client,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[BackedDeposit]:
    """
    Args:
        organization_id (str):
        guild_id (str):
        deposit_id (str):
        offset (Union[Unset, None, int]):

    Returns:
        Response[BackedDeposit]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            guild_id=guild_id,
            deposit_id=deposit_id,
            client=client,
            offset=offset,
        )
    ).parsed
