"""
Pure Base64 encoding/decoding helpers.

This module contains no user interaction and no CLI logic.
"""

from __future__ import annotations

import base64
import binascii

from .exceptions import (
    InvalidBase64Error,
    InvalidEncodingError,
)


def encode_text(
    text: str,
    *,
    encoding: str = "utf-8",
) -> str:
    """
    Encode Unicode text to Base64.
    """
    try:
        raw = text.encode(encoding)
    except LookupError as exc:
        raise InvalidEncodingError(f"Unknown encoding: {encoding}") from exc

    return base64.b64encode(raw).decode("ascii")


def decode_text(
    data: str,
    *,
    encoding: str = "utf-8",
    validate: bool = True,
) -> str:
    """
    Decode Base64 into Unicode text.
    """
    try:
        raw = base64.b64decode(data, validate=validate)
    except (binascii.Error, ValueError) as exc:
        raise InvalidBase64Error("Invalid Base64 data.") from exc

    try:
        return raw.decode(encoding)
    except LookupError as exc:
        raise InvalidEncodingError(f"Unknown encoding: {encoding}") from exc
