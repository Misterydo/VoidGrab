"""Argument parser for the VoidGrab CLI."""

from __future__ import annotations

import argparse

DOWNLOAD_TARGETS = ("all", "video", "audio", "thumb", "comments", "subtitles")
LIST_TARGETS = ("info", "formats", "profile")


class VoidGrabArgumentParser(argparse.ArgumentParser):
    """Custom parser that validates VoidGrab command combinations."""

    def error(self, message: str) -> None:  # pragma: no cover - argparse exits
        super().error(message)


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = VoidGrabArgumentParser(
        prog="voidgrab",
        description="VoidGrab: universal media detector, metadata extractor, and downloader.",
    )
    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument("--download", metavar="TARGET", help="Download target: all, video, audio, thumb, format=ID.")
    action_group.add_argument("--list", choices=LIST_TARGETS, metavar="TARGET", help="List target: info, formats, profile.")
    action_group.add_argument("--extract", choices=("raw",), metavar="TARGET", help="Extract raw platform data without downloading.")
    parser.add_argument("url", metavar="URL", help="Media or social URL to process.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--output", default="downloads", help="Output directory for downloads and exported files.")
    return parser


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse and validate CLI arguments."""
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.download and not (args.download in DOWNLOAD_TARGETS or args.download.startswith("format=")):
        parser.error("--download must be one of all, video, audio, thumb, comments, subtitles, or format=ID")
    return args
