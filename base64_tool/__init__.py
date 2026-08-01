"""
Base64 Interactive Tool.

A small, testable and maintainable Base64 encoder/decoder.
"""

from .exceptions import (
    Base64ToolError,
    InvalidBase64Error,
    InvalidEncodingError,
    InvalidFileError,
)

__all__ = [
    "Base64ToolError",
    "InvalidBase64Error",
    "InvalidEncodingError",
    "InvalidFileError",
]
