"""Threads platform module."""

from __future__ import annotations

from voidgrab.platforms.base import BasePlatform


class PlatformModule(BasePlatform):
    name = "threads"
    display_name = "Threads"
    domains = ("threads.net",)
