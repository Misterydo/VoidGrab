"""JSON output helpers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def dumps(data: Any) -> str:
    """Serialize data as pretty UTF-8 JSON text."""
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)


def write_json(path: str | Path, data: Any) -> Path:
    """Write data to a JSON file."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(dumps(data) + "\n", encoding="utf-8")
    return target
