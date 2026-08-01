from base64_tool.exceptions import (
    Base64ToolError,
    InvalidBase64Error,
    InvalidEncodingError,
    InvalidFileError,
)


def test_exception_hierarchy():
    assert issubclass(InvalidBase64Error, Base64ToolError)
    assert issubclass(InvalidEncodingError, Base64ToolError)
    assert issubclass(InvalidFileError, Base64ToolError)
