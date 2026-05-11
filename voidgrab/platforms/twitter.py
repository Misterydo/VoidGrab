"""Twitter/X platform module."""

from __future__ import annotations

from voidgrab.platforms.base import BasePlatform


class PlatformModule(BasePlatform):
    name = "twitter"
    display_name = "Twitter/X"
    domains = ("twitter.com", "x.com", "t.co")
