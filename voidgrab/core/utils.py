"""Small utility helpers used across VoidGrab."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse

_SLUG_RE = re.compile(r"[^a-zA-Z0-9._-]+")


def normalize_domain(url: str) -> str:
    """Return a lower-case hostname stripped of a leading www."""
    parsed = urlparse(url)
    host = parsed.netloc or parsed.path.split("/", 1)[0]
    host = host.lower().split("@")[-1].split(":", 1)[0]
    return host[4:] if host.startswith("www.") else host


def slugify(value: str | None, fallback: str = "media") -> str:
    """Create a filesystem-friendly slug."""
    if not value:
        return fallback
    slug = _SLUG_RE.sub("_", value.strip()).strip("._-")
    return slug[:80] or fallback


def ensure_directory(path: str | Path) -> Path:
    """Create a directory and return it as a Path."""
    directory = Path(path).expanduser().resolve()
    directory.mkdir(parents=True, exist_ok=True)
    return directory
