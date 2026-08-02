#!/usr/bin/env python3
"""
Generate repository digest with proper UTF-8 encoding.

Fixes cp1252 codec errors on Windows.
"""

import os
import sys


def generate_digest(root_dir, output_file):
    """Walk directory tree and write all file contents to digest."""

    with open(output_file, "w", encoding="utf-8") as out:
        out.write("Directory structure:\n")

        for dirpath, dirnames, filenames in os.walk(root_dir):
            dirnames[:] = [
                d
                for d in dirnames
                if d
                not in (
                    ".git",
                    "__pycache__",
                    "node_modules",
                )
            ]

            level = dirpath.replace(root_dir, "").count(os.sep)
            indent = "│   " * level
            out.write(f"{indent}├── {os.path.basename(dirpath)}/\n")

            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(filepath, root_dir)

                out.write(f"\n{'=' * 50}\n")
                out.write(f"FILE: {rel_path}\n")
                out.write(f"{'=' * 50}\n")

                try:
                    with open(filepath, encoding="utf-8") as f:
                        out.write(f.read())
                        out.write("\n")

                except UnicodeDecodeError as e:
                    out.write(f"[BINARY/ENCODED FILE] {e}\n")

                except Exception as e:
                    out.write(f"[ERROR] {e}\n")

    print(f"[OK] Digest generated: {output_file}")


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    output = sys.argv[2] if len(sys.argv) > 2 else "digest.txt"

    generate_digest(root, output)
