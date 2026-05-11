"""Download orchestration primitives."""

from __future__ import annotations

from typing import Any


class DownloadEngine:
    """Delegates downloads to routed platform modules.

    The engine intentionally receives already-routed platform modules and keeps
    download separate from extraction, so future cache/fallback strategies can
    reuse extracted data without re-downloading.
    """

    async def download(self, platform: Any, url: str, media_format: str, output: str | None = None) -> dict[str, Any]:
        """Download the requested media target using the selected platform."""
        return await platform.download(url, media_format, output)
