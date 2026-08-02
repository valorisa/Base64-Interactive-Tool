"""
Command-line interface for Base64 Interactive Tool.
"""

from __future__ import annotations

import argparse
import sys

from .codec import decode_text, encode_text
from .exceptions import Base64ToolError
from .files import decode_file, encode_file


def cmd_encode(args: argparse.Namespace) -> int:
    """Encode text to Base64."""
    print(encode_text(args.text, encoding=args.encoding))
    return 0


def cmd_decode(args: argparse.Namespace) -> int:
    """Decode Base64 text."""
    print(decode_text(args.text, encoding=args.encoding))
    return 0


def cmd_encode_file(args: argparse.Namespace) -> int:
    """Encode a text file to Base64."""
    encode_file(
        args.source,
        args.destination,
        encoding=args.encoding,
    )
    return 0


def cmd_decode_file(args: argparse.Namespace) -> int:
    """Decode a Base64 file."""
    decode_file(
        args.source,
        args.destination,
        encoding=args.encoding,
    )
    return 0


COMMANDS = {
    "encode": cmd_encode,
    "decode": cmd_decode,
    "encode-file": cmd_encode_file,
    "decode-file": cmd_decode_file,
}


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(
        prog="base64-tool",
        description="Base64 Interactive Tool",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    text_commands = {
        "encode",
        "decode",
    }

    for name in COMMANDS:
        sub = subparsers.add_parser(name)

        if name in text_commands:
            sub.add_argument(
                "text",
                help="Input text.",
            )
        else:
            sub.add_argument(
                "source",
                help="Input file.",
            )
            sub.add_argument(
                "destination",
                help="Output file.",
            )

        sub.add_argument(
            "--encoding",
            default="utf-8",
            help="Text encoding (default: utf-8).",
        )

    return parser


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        return COMMANDS[args.command](args)
    except Base64ToolError as exc:
        print(exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
