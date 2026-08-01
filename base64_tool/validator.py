"""
Validation helpers.

This module centralizes input validation independently from the
encoding/decoding logic.
"""

from __future__ import annotations

import base64
import binascii
import codecs

from .exceptions import (
    InvalidBase64Error,
    InvalidEncodingError,
)


def is_base64(data: str) -> bool:
    """
    Return True if *data* is valid Base64.
    """
    try:
        base64.b64decode(data, validate=True)
        return True
    except (binascii.Error, ValueError):
        return False


def require_base64(data: str) -> None:
    """
    Ensure that *data* is valid Base64.
    """
    if not is_base64(data):
        raise InvalidBase64Error("Invalid Base64 data.")


def require_encoding(name: str) -> None:
    """
    Ensure that *name* is a valid Python encoding.
    """
    try:
        codecs.lookup(name)
    except LookupError as exc:
        raise InvalidEncodingError(
            f"Unknown encoding: {name}"
        ) from exc


def require_text(value: object) -> None:
    """
    Ensure that *value* is a Unicode string.
    """
    if not isinstance(value, str):
        raise TypeError("Expected a string.")
