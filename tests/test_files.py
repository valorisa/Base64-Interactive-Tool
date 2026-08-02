from pathlib import Path

import pytest

from base64_tool.exceptions import (
    InvalidBase64Error,
    InvalidEncodingError,
    InvalidFileError,
)
from base64_tool.files import (
    decode_file,
    encode_file,
)


def test_encode_file(tmp_path: Path):
    source = tmp_path / "input.txt"
    destination = tmp_path / "output.b64"

    source.write_text("hello", encoding="utf-8")

    encode_file(source, destination)

    assert destination.read_text(encoding="ascii") == "aGVsbG8="


def test_decode_file(tmp_path: Path):
    source = tmp_path / "input.b64"
    destination = tmp_path / "output.txt"

    source.write_text("aGVsbG8=", encoding="ascii")

    decode_file(source, destination)

    assert destination.read_text(encoding="utf-8") == "hello"


def test_roundtrip_file(tmp_path: Path):
    original = tmp_path / "original.txt"
    encoded = tmp_path / "encoded.b64"
    decoded = tmp_path / "decoded.txt"

    text = "Bonjour le monde"

    original.write_text(text, encoding="utf-8")

    encode_file(original, encoded)
    decode_file(encoded, decoded)

    assert decoded.read_text(encoding="utf-8") == text


def test_encode_missing_file(tmp_path: Path):
    with pytest.raises(InvalidFileError):
        encode_file(
            tmp_path / "missing.txt",
            tmp_path / "output.b64",
        )


def test_decode_missing_file(tmp_path: Path):
    with pytest.raises(InvalidFileError):
        decode_file(
            tmp_path / "missing.b64",
            tmp_path / "output.txt",
        )


def test_decode_invalid_base64(tmp_path: Path):
    source = tmp_path / "invalid.b64"
    destination = tmp_path / "output.txt"

    source.write_text("%%%%", encoding="ascii")

    with pytest.raises(InvalidBase64Error):
        decode_file(source, destination)


def test_unknown_encoding_encode(tmp_path: Path):
    source = tmp_path / "input.txt"
    destination = tmp_path / "output.b64"

    source.write_text("hello", encoding="utf-8")

    with pytest.raises(InvalidEncodingError):
        encode_file(
            source,
            destination,
            encoding="does-not-exist",
        )


def test_unknown_encoding_decode(tmp_path: Path):
    source = tmp_path / "input.b64"
    destination = tmp_path / "output.txt"

    source.write_text("aGVsbG8=", encoding="ascii")

    with pytest.raises(InvalidEncodingError):
        decode_file(
            source,
            destination,
            encoding="does-not-exist",
        )
