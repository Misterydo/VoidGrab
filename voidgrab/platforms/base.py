"""Base class for VoidGrab platform modules."""

from __future__ import annotations

from typing import Any, ClassVar

from voidgrab.core.metadata import MediaMetadata
from voidgrab.core.utils import normalize_domain


class BasePlatform:
    """Minimal platform contract used by the router and extractor engine."""

    name: ClassVar[str] = "base"
    display_name: ClassVar[str] = "Base"
    domains: ClassVar[tuple[str, ...]] = ()

    async def match(self, url: str) -> bool:
        """Return whether this platform supports the URL."""
        domain = normalize_domain(url)
        return any(domain == supported or domain.endswith(f".{supported}") for supported in self.domains)

    async def extract_metadata(self, url: str) -> dict[str, Any]:
        """Return safe baseline metadata; concrete modules can enrich this."""
        return MediaMetadata(platform=self.display_name, url=url).to_dict()

    async def list_formats(self, url: str) -> list[dict[str, Any]]:
        """Return available formats; empty until a platform implements extraction."""
        return []

    async def download(self, url: str, media_format: str, output: str | None = None) -> dict[str, Any]:
        """Placeholder download contract for future download engine integration."""
        raise NotImplementedError(f"Download is not implemented for {self.display_name} yet.")
