from __future__ import annotations

import asyncio

import pytest

from voidgrab.core.router import PlatformRouter


@pytest.mark.parametrize(
    ("url", "platform"),
    [
        ("https://youtube.com/watch?v=abc", "youtube"),
        ("https://youtu.be/abc", "youtube"),
        ("https://www.tiktok.com/@user/video/1", "tiktok"),
        ("https://instagram.com/p/abc/", "instagram"),
        ("https://redd.it/abc", "reddit"),
        ("https://x.com/user/status/1", "twitter"),
        ("https://threads.net/@user/post/1", "threads"),
    ],
)
def test_router_detects_supported_platforms(url: str, platform: str) -> None:
    route = asyncio.run(PlatformRouter().detect(url))

    assert route.platform.name == platform
    assert route.url == url


def test_router_rejects_unsupported_platform() -> None:
    with pytest.raises(ValueError, match="Unsupported platform"):
        asyncio.run(PlatformRouter().detect("https://example.com/video"))
