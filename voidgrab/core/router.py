"""Platform detection and routing."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from voidgrab.core.utils import normalize_domain
from voidgrab.platforms import instagram, reddit, threads, tiktok, twitter, youtube
from voidgrab.platforms.base import BasePlatform


@dataclass(slots=True)
class RouteResult:
    """Result of URL platform detection."""

    platform: BasePlatform
    url: str


class PlatformRouter:
    """Detects the best platform module for a URL."""

    def __init__(self, platforms: Iterable[BasePlatform] | None = None) -> None:
        self.platforms = list(platforms or default_platforms())

    async def detect(self, url: str) -> RouteResult:
        """Return the first platform that matches the URL."""
        for platform in self.platforms:
            if await platform.match(url):
                return RouteResult(platform=platform, url=url)
        domain = normalize_domain(url)
        raise ValueError(f"Unsupported platform for domain: {domain or url}")


def default_platforms() -> list[BasePlatform]:
    """Instantiate built-in platform modules."""
    return [
        youtube.PlatformModule(),
        tiktok.PlatformModule(),
        instagram.PlatformModule(),
        reddit.PlatformModule(),
        twitter.PlatformModule(),
        threads.PlatformModule(),
    ]
