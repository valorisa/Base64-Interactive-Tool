import pytest

from base64_tool.codec import (
    decode_text,
    encode_text,
)
from base64_tool.exceptions import (
    InvalidBase64Error,
    InvalidEncodingError,
)


def test_encode_text():
    assert encode_text("hello") == "aGVsbG8="


def test_decode_text():
    assert decode_text("aGVsbG8=") == "hello"


def test_roundtrip():
    text = "Bonjour le monde"
    assert decode_text(encode_text(text)) == text


def test_invalid_base64():
    with pytest.raises(InvalidBase64Error):
        decode_text("%%%%")


def test_unknown_encoding_encode():
    with pytest.raises(InvalidEncodingError):
        encode_text("hello", encoding="does-not-exist")


def test_unknown_encoding_decode():
    with pytest.raises(InvalidEncodingError):
        decode_text("aGVsbG8=", encoding="does-not-exist")
