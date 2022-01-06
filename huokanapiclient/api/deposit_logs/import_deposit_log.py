from typing import Any, Dict

import httpx

from ...client import Client
from ...models.deposit_log import DepositLog
from ...types import Response


def _get_kwargs(
    organization_id: str,
    guild_id: str,
    *,
    client: Client,
    json_body: DepositLog,
) -> Dict[str, Any]:
    url = "{}/organizations/{organizationId}/guilds/{guildId}/depositLogs".format(
        client.base_url, organizationId=organization_id, guildId=guild_id
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: DepositLog,
) -> Response[Any]:
    """
    Args:
        organization_id (str):
        guild_id (str):
        json_body (DepositLog):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        guild_id=guild_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    organization_id: str,
    guild_id: str,
    *,
    client: Client,
    json_body: DepositLog,
) -> Response[Any]:
    """
    Args:
        organization_id (str):
        guild_id (str):
        json_body (DepositLog):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        guild_id=guild_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
