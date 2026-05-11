# VoidGrab

VoidGrab is a modular **media detector + metadata extractor + downloader** CLI.
The project is intentionally split between extraction and download so metadata,
format listing, cache, and future fallback extractors can evolve independently.

## Phase 1 scope

The current implementation provides the initial CLI foundation:

- command parser for `--download`, `--list`, and `--extract` workflows;
- automatic platform detection through a router;
- baseline platform modules for YouTube, TikTok, Instagram, Reddit, Twitter/X,
  and Threads;
- human-readable and JSON output helpers;
- output folder helpers for the future download engine.

## Usage

```bash
voidgrab --list info URL
voidgrab --list info URL --json
voidgrab --list formats URL
voidgrab --extract raw URL
voidgrab --download audio URL
voidgrab --download format=137 URL --output ./downloads
```

Downloads are wired through the engine contract but concrete media downloading is
not implemented yet. This keeps Phase 1 focused on routing, CLI ergonomics, and
module boundaries.

## Architecture

```text
URL
 ↓
Router
 ↓
Platform Module
 ↓
Extractor
 ↓
Metadata / Format Formatter
 ↓
Download Engine or Exporter
```

Repository layout:

```text
voidgrab/
├── core/       # router, extraction, download contracts, formatting, utilities
├── platforms/  # platform modules implementing the common module contract
├── outputs/    # JSON/TXT/folder organization helpers
├── cli/        # parser, commands, terminal interface
└── main.py     # console entry point
```

## Development

```bash
python -m pytest
python -m voidgrab.main --list info https://youtu.be/example --json
```
