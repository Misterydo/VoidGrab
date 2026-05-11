"""Plain-text output helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from voidgrab.core.formatter import format_info


def dumps(metadata: dict[str, Any]) -> str:
    """Serialize metadata as human-readable text."""
    return format_info(metadata)


def write_txt(path: str | Path, metadata: dict[str, Any]) -> Path:
    """Write metadata to a plain-text file."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(dumps(metadata) + "\n", encoding="utf-8")
    return target
