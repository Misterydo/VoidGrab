"""Output folder organization."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from voidgrab.core.utils import ensure_directory, slugify


def build_media_folder(base_output: str | Path, metadata: dict[str, Any]) -> Path:
    """Build downloads/<Platform>/<title_or_media>_<views_or_id>/ style folders."""
    platform = slugify(str(metadata.get("platform") or "Unknown"), "Unknown")
    title = slugify(str(metadata.get("title") or "media"), "media")
    suffix = metadata.get("views") or metadata.get("id") or "item"
    folder = ensure_directory(base_output) / platform / f"{title}_{slugify(str(suffix), 'item')}"
    folder.mkdir(parents=True, exist_ok=True)
    return folder
