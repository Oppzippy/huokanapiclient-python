from typing import Any, Dict

import httpx

from ...client import Client
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    redirect_url: str,
) -> Dict[str, Any]:
    url = "{}/authorization/discord/redirect".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "redirectUrl": redirect_url,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    redirect_url: str,
) -> Response[Any]:
    """
    Args:
        redirect_url (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        redirect_url=redirect_url,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    redirect_url: str,
) -> Response[Any]:
    """
    Args:
        redirect_url (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        redirect_url=redirect_url,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
