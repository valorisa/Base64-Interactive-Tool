"""
Custom exceptions for Base64 Interactive Tool.

All project-specific exceptions derive from Base64ToolError.
"""

from __future__ import annotations


class Base64ToolError(Exception):
    """Base class for all project exceptions."""


class InvalidBase64Error(Base64ToolError):
    """Raised when Base64 input is invalid."""


class InvalidEncodingError(Base64ToolError):
    """Raised when a text encoding is unsupported."""


class InvalidFileError(Base64ToolError):
    """Raised when a file cannot be processed."""
