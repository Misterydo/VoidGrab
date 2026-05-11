"""Reddit platform module."""

from __future__ import annotations

from voidgrab.platforms.base import BasePlatform


class PlatformModule(BasePlatform):
    name = "reddit"
    display_name = "Reddit"
    domains = ("reddit.com", "redd.it")
