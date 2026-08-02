"""
File encoding and decoding helpers.

This module provides high-level helpers for encoding and decoding files
using the pure functions defined in codec.py.
"""

from __future__ import annotations

from pathlib import Path

from .codec import decode_text, encode_text
from .exceptions import InvalidFileError
from .validator import require_encoding


def encode_file(
    source: str | Path,
    destination: str | Path,
    *,
    encoding: str = "utf-8",
) -> None:
    """
    Encode a text file into a Base64 file.
    """
    require_encoding(encoding)

    source = Path(source)
    destination = Path(destination)

    try:
        text = source.read_text(encoding=encoding)
        encoded = encode_text(text, encoding=encoding)
        destination.write_text(encoded, encoding="ascii")
    except OSError as exc:
        raise InvalidFileError(str(exc)) from exc


def decode_file(
    source: str | Path,
    destination: str | Path,
    *,
    encoding: str = "utf-8",
) -> None:
    """
    Decode a Base64 file into a text file.
    """
    require_encoding(encoding)

    source = Path(source)
    destination = Path(destination)

    try:
        encoded = source.read_text(encoding="ascii")
        decoded = decode_text(encoded, encoding=encoding)
        destination.write_text(decoded, encoding=encoding)
    except OSError as exc:
        raise InvalidFileError(str(exc)) from exc
