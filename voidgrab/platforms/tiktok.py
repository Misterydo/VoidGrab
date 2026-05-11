"""TikTok platform module."""

from __future__ import annotations

from voidgrab.platforms.base import BasePlatform


class PlatformModule(BasePlatform):
    name = "tiktok"
    display_name = "TikTok"
    domains = ("tiktok.com", "vm.tiktok.com")
