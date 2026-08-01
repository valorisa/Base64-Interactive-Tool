"""
Interactive interface.

This module provides a simple interactive prompt while delegating all
business logic to the codec and validator modules.
"""

from __future__ import annotations

from .codec import decode_text, encode_text
from .exceptions import Base64ToolError
from .validator import require_encoding


def run() -> int:
    """
    Run the interactive Base64 tool.

    Returns
    -------
    int
        Process exit status.
    """
    print("Base64 Interactive Tool")
    print()

    mode = input("(E)ncode or (D)ecode? ").strip().lower()

    if mode not in {"e", "d"}:
        print("Invalid choice.")
        return 1

    encoding = input("Encoding [utf-8]: ").strip() or "utf-8"

    try:
        require_encoding(encoding)

        text = input("Input: ")

        if mode == "e":
            result = encode_text(text, encoding=encoding)
        else:
            result = decode_text(text, encoding=encoding)

    except Base64ToolError as exc:
        print(f"Error: {exc}")
        return 1

    print()
    print("Result:")
    print(result)

    return 0
