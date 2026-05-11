"""Shared metadata structures for VoidGrab."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class MediaMetadata:
    """Normalized metadata returned by platform extractors."""

    title: str | None = None
    author: str | None = None
    likes: int | None = None
    views: int | None = None
    duration: int | float | None = None
    upload_date: str | None = None
    platform: str | None = None
    url: str | None = None
    description: str | None = None
    raw: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable metadata dictionary without empty fields."""
        data = {
            "title": self.title,
            "author": self.author,
            "likes": self.likes,
            "views": self.views,
            "duration": self.duration,
            "upload_date": self.upload_date,
            "platform": self.platform,
            "url": self.url,
            "description": self.description,
            "raw": self.raw or None,
        }
        return {key: value for key, value in data.items() if value is not None}
