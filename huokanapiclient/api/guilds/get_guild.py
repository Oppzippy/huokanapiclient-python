from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.guild import Guild
from ...types import Response


def _get_kwargs(
    organization_id: str,
    guild_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/organizations/{organizationId}/guilds/{guildId}".format(
        client.base_url, organizationId=organization_id, guildId=guild_id
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Guild]:
    if response.status_code == 200:
        response_200 = Guild.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Guild]:
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
) -> Response[Guild]:
    """
    Args:
        organization_id (str):
        guild_id (str):

    Returns:
        Response[Guild]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        guild_id=guild_id,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    organization_id: str,
    guild_id: str,
    *,
    client: Client,
) -> Optional[Guild]:
    """
    Args:
        organization_id (str):
        guild_id (str):

    Returns:
        Response[Guild]
    """

    return sync_detailed(
        organization_id=organization_id,
        guild_id=guild_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    guild_id: str,
    *,
    client: Client,
) -> Response[Guild]:
    """
    Args:
        organization_id (str):
        guild_id (str):

    Returns:
        Response[Guild]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        guild_id=guild_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    organization_id: str,
    guild_id: str,
    *,
    client: Client,
) -> Optional[Guild]:
    """
    Args:
        organization_id (str):
        guild_id (str):

    Returns:
        Response[Guild]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            guild_id=guild_id,
            client=client,
        )
    ).parsed
