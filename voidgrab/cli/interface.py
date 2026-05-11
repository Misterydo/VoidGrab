"""CLI entry helpers."""

from __future__ import annotations

import asyncio
import sys
from collections.abc import Sequence

from voidgrab.cli.commands import run_command
from voidgrab.cli.parser import parse_args


def run(argv: Sequence[str] | None = None) -> int:
    """Run the VoidGrab CLI."""
    args = parse_args(list(argv) if argv is not None else None)
    try:
        code, output = asyncio.run(run_command(args))
    except ValueError as exc:
        print(f"voidgrab: error: {exc}", file=sys.stderr)
        return 2
    except NotImplementedError as exc:
        print(f"voidgrab: {exc}", file=sys.stderr)
        return 1
    if output:
        print(output)
    return code
