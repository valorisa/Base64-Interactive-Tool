# API Reference

## Overview

The public API intentionally remains small.

Business logic is implemented as pure functions located in
`base64_tool.codec`.

Validation helpers are available in
`base64_tool.validator`.

Project-specific exceptions are defined in
`base64_tool.exceptions`.

## Codec

### `encode_text()`

```python
encode_text(
    text: str,
    *,
    encoding: str = "utf-8",
) -> str
```

Encode Unicode text into a Base64 string.

#### Parameters

| Name | Type | Description |
| ---- | ---- | ----------- |
| `text` | `str` | Text to encode |
| `encoding` | `str` | Source character encoding |

#### Returns

A Base64-encoded ASCII string.

#### Raises

- `InvalidEncodingError`

---

### `decode_text()`

```python
decode_text(
    data: str,
    *,
    encoding: str = "utf-8",
    validate: bool = True,
) -> str
```

Decode a Base64 string into Unicode text.

#### Parameters

| Name | Type | Description |
| ---- | ---- | ----------- |
| `data` | `str` | Base64 input |
| `encoding` | `str` | Target character encoding |
| `validate` | `bool` | Reject malformed Base64 |

#### Returns

Decoded Unicode text.

#### Raises

- `InvalidBase64Error`
- `InvalidEncodingError`

---

## Validator

### `is_base64()`

Return `True` if the supplied string is valid Base64.

### `require_base64()`

Validate Base64 input.

Raises `InvalidBase64Error` on failure.

### `require_encoding()`

Validate a Python encoding name.

Raises `InvalidEncodingError` on failure.

### `require_text()`

Ensure that the supplied value is a string.

Raises `TypeError` otherwise.

---

## Exceptions

The project exposes the following exception hierarchy.

```text
Base64ToolError
├── InvalidBase64Error
├── InvalidEncodingError
└── InvalidFileError
```

Applications are encouraged to catch
`Base64ToolError`
when handling project-specific failures.

---

## Stability

The public API follows semantic versioning.

Public functions documented here are intended to remain
backward compatible throughout the 2.x series.

