from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.authorization import Authorization
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    code: str,
    redirect_url: str,
) -> Dict[str, Any]:
    url = "{}/authorization/discord/authorize".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "code": code,
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


def _parse_response(*, response: httpx.Response) -> Optional[Authorization]:
    if response.status_code == 200:
        response_200 = Authorization.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Authorization]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    code: str,
    redirect_url: str,
) -> Response[Authorization]:
    """
    Args:
        code (str):
        redirect_url (str):

    Returns:
        Response[Authorization]
    """

    kwargs = _get_kwargs(
        client=client,
        code=code,
        redirect_url=redirect_url,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    code: str,
    redirect_url: str,
) -> Optional[Authorization]:
    """
    Args:
        code (str):
        redirect_url (str):

    Returns:
        Response[Authorization]
    """

    return sync_detailed(
        client=client,
        code=code,
        redirect_url=redirect_url,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    code: str,
    redirect_url: str,
) -> Response[Authorization]:
    """
    Args:
        code (str):
        redirect_url (str):

    Returns:
        Response[Authorization]
    """

    kwargs = _get_kwargs(
        client=client,
        code=code,
        redirect_url=redirect_url,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    code: str,
    redirect_url: str,
) -> Optional[Authorization]:
    """
    Args:
        code (str):
        redirect_url (str):

    Returns:
        Response[Authorization]
    """

    return (
        await asyncio_detailed(
            client=client,
            code=code,
            redirect_url=redirect_url,
        )
    ).parsed
