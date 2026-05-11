from __future__ import annotations

import json

from voidgrab.cli.interface import run
from voidgrab.cli.parser import parse_args


def test_parse_download_format_target() -> None:
    args = parse_args(["--download", "format=137", "https://youtube.com/watch?v=abc"])

    assert args.download == "format=137"
    assert args.url == "https://youtube.com/watch?v=abc"


def test_cli_lists_info_as_json(capsys) -> None:
    code = run(["--list", "info", "https://youtu.be/abc", "--json"])

    captured = capsys.readouterr()
    assert code == 0
    payload = json.loads(captured.out)
    assert payload["platform"] == "YouTube"
    assert payload["url"] == "https://youtu.be/abc"


def test_cli_reports_unimplemented_download(capsys) -> None:
    code = run(["--download", "audio", "https://youtu.be/abc"])

    captured = capsys.readouterr()
    assert code == 1
    assert "not implemented" in captured.err
