import pytest

from base64_tool.exceptions import (
    InvalidBase64Error,
    InvalidEncodingError,
)
from base64_tool.validator import (
    is_base64,
    require_base64,
    require_encoding,
    require_text,
)


def test_is_base64_valid():
    assert is_base64("aGVsbG8=")


def test_is_base64_invalid():
    assert not is_base64("%%%%")


def test_require_base64_valid():
    require_base64("aGVsbG8=")


def test_require_base64_invalid():
    with pytest.raises(InvalidBase64Error):
        require_base64("%%%%")


def test_require_encoding_valid():
    require_encoding("utf-8")
    require_encoding("latin-1")


def test_require_encoding_invalid():
    with pytest.raises(InvalidEncodingError):
        require_encoding("does-not-exist")


def test_require_text_valid():
    require_text("hello")


def test_require_text_invalid():
    with pytest.raises(TypeError):
        require_text(123)
