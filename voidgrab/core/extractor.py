"""Extraction orchestration helpers."""

from __future__ import annotations

from typing import Any, Protocol


class PlatformProtocol(Protocol):
    """Protocol every platform module implements."""

    name: str
    display_name: str

    async def extract_metadata(self, url: str) -> dict[str, Any]: ...

    async def list_formats(self, url: str) -> list[dict[str, Any]]: ...


class ExtractorEngine:
    """Coordinates metadata and format extraction for a routed platform."""

    async def extract_metadata(self, platform: PlatformProtocol, url: str) -> dict[str, Any]:
        """Extract normalized metadata without downloading media."""
        return await platform.extract_metadata(url)

    async def list_formats(self, platform: PlatformProtocol, url: str) -> list[dict[str, Any]]:
        """List available media formats without downloading media."""
        return await platform.list_formats(url)
