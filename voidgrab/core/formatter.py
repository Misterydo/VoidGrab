"""Terminal formatting for VoidGrab CLI output."""

from __future__ import annotations

from typing import Any


def format_info(metadata: dict[str, Any]) -> str:
    """Render metadata as human-readable text."""
    labels = {
        "title": "Title",
        "author": "Author",
        "platform": "Platform",
        "views": "Views",
        "likes": "Likes",
        "duration": "Duration",
        "upload_date": "Upload date",
        "url": "URL",
        "description": "Description",
    }
    lines = [f"{label}: {metadata[key]}" for key, label in labels.items() if metadata.get(key) is not None]
    return "\n".join(lines) if lines else "No metadata available."


def format_formats(formats: list[dict[str, Any]]) -> str:
    """Render a compact format table."""
    if not formats:
        return "No formats available."

    headers = ("ID", "RESOLUTION", "CODEC", "BITRATE", "FPS", "SIZE")
    rows = [
        (
            str(item.get("id", "-")),
            str(item.get("resolution", "-")),
            str(item.get("codec", "-")),
            str(item.get("bitrate", "-")),
            str(item.get("fps", "-")),
            str(item.get("size", "-")),
        )
        for item in formats
    ]
    widths = [max(len(headers[index]), *(len(row[index]) for row in rows)) for index in range(len(headers))]
    lines = ["  ".join(header.ljust(widths[index]) for index, header in enumerate(headers))]
    lines.extend("  ".join(value.ljust(widths[index]) for index, value in enumerate(row)) for row in rows)
    return "\n".join(lines)
