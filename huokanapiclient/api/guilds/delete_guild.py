from typing import Any, Dict

import httpx

from ...client import Client
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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    organization_id: str,
    guild_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """
    Args:
        organization_id (str):
        guild_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        guild_id=guild_id,
        client=client,
    )

    response = httpx.delete(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    organization_id: str,
    guild_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """
    Args:
        organization_id (str):
        guild_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        guild_id=guild_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)
