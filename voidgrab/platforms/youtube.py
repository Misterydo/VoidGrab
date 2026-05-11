"""YouTube platform module."""

from __future__ import annotations

from voidgrab.platforms.base import BasePlatform


class PlatformModule(BasePlatform):
    name = "youtube"
    display_name = "YouTube"
    domains = ("youtube.com", "youtu.be", "youtube-nocookie.com")
