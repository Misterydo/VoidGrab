"""Command handlers for VoidGrab."""

from __future__ import annotations

from argparse import Namespace
from typing import Any

from voidgrab.core.downloader import DownloadEngine
from voidgrab.core.extractor import ExtractorEngine
from voidgrab.core.formatter import format_formats, format_info
from voidgrab.core.router import PlatformRouter
from voidgrab.outputs import json_export


async def run_command(args: Namespace) -> tuple[int, str]:
    """Run a parsed CLI command and return an exit code plus printable output."""
    router = PlatformRouter()
    route = await router.detect(args.url)
    extractor = ExtractorEngine()

    if args.list == "info":
        metadata = await extractor.extract_metadata(route.platform, route.url)
        return 0, json_export.dumps(metadata) if args.json else format_info(metadata)

    if args.list == "formats":
        formats = await extractor.list_formats(route.platform, route.url)
        return 0, json_export.dumps(formats) if args.json else format_formats(formats)

    if args.list == "profile":
        payload: dict[str, Any] = {"platform": route.platform.display_name, "url": route.url, "profile": None}
        return 0, json_export.dumps(payload) if args.json else "Profile extraction is not implemented yet."

    if args.extract == "raw":
        metadata = await extractor.extract_metadata(route.platform, route.url)
        payload = {"platform": route.platform.name, "url": route.url, "raw": metadata.get("raw", metadata)}
        return 0, json_export.dumps(payload)

    if args.download:
        downloader = DownloadEngine()
        result = await downloader.download(route.platform, route.url, args.download, args.output)
        return 0, json_export.dumps(result) if args.json else f"Downloaded {args.download} to {result.get('path', args.output)}"

    return 2, "No command selected."
