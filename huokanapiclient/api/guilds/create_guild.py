from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.guild import Guild
from ...models.guild_partial import GuildPartial
from ...types import Response


def _get_kwargs(
    organization_id: str,
    *,
    client: Client,
    json_body: GuildPartial,
) -> Dict[str, Any]:
    url = "{}/organizations/{organizationId}/guilds".format(client.base_url, organizationId=organization_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    *,
    client: Client,
    json_body: GuildPartial,
) -> Response[Guild]:
    """
    Args:
        organization_id (str):
        json_body (GuildPartial):

    Returns:
        Response[Guild]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    organization_id: str,
    *,
    client: Client,
    json_body: GuildPartial,
) -> Optional[Guild]:
    """
    Args:
        organization_id (str):
        json_body (GuildPartial):

    Returns:
        Response[Guild]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Client,
    json_body: GuildPartial,
) -> Response[Guild]:
    """
    Args:
        organization_id (str):
        json_body (GuildPartial):

    Returns:
        Response[Guild]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Client,
    json_body: GuildPartial,
) -> Optional[Guild]:
    """
    Args:
        organization_id (str):
        json_body (GuildPartial):

    Returns:
        Response[Guild]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
