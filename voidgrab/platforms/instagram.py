"""Instagram platform module."""

from __future__ import annotations

from voidgrab.platforms.base import BasePlatform


class PlatformModule(BasePlatform):
    name = "instagram"
    display_name = "Instagram"
    domains = ("instagram.com",)
