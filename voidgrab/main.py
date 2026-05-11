"""Module entry point for VoidGrab."""

from __future__ import annotations

from voidgrab.cli.interface import run


def main() -> int:
    """Console script entry point."""
    return run()


if __name__ == "__main__":
    raise SystemExit(main())
