# Base64 Interactive Tool

![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A lightweight, testable and maintainable Base64 encoder/decoder written in
pure Python.

This project demonstrates how a small Python script can evolve into a clean,
well-structured and professionally organized command-line application while
remaining easy to understand.

---

## Features

- Encode Unicode text to Base64
- Decode Base64 strings into Unicode text
- Interactive mode
- Command-line interface
- Pure business logic
- Dedicated exception hierarchy
- Modular architecture
- Comprehensive unit tests
- Modern Python package layout
- Easy to extend and maintain

---

## Requirements

- Python 3.11 or newer

---

## Installation

Clone the repository:

```bash
git clone https://github.com/valorisa/base64-interactive-tool.git

cd base64-interactive-tool
```

Install in editable mode:

```bash
python -m pip install -e .
```

---

## Usage

### Encode text

```bash
base64-tool encode "hello"
```

Output

```text
aGVsbG8=
```

### Decode text

```bash
base64-tool decode "aGVsbG8="
```

Output

```text
hello
```

### Interactive mode

```bash
python -m base64_tool
```

---

## Project Structure

```text
base64_tool/
├── __init__.py
├── __main__.py
├── cli.py
├── codec.py
├── exceptions.py
├── interactive.py
└── validator.py

docs/
tests/
```

---

## Architecture

The project is intentionally organized around small modules with a single
responsibility.

| Module | Responsibility |
| ------- | -------------- |
| `codec.py` | Base64 encoding and decoding |
| `validator.py` | Input validation |
| `interactive.py` | Interactive user interface |
| `cli.py` | Command-line interface |
| `exceptions.py` | Project-specific exceptions |

---

## Development

Run the complete test suite:

```bash
python -m pytest
```

Compile every module:

```bash
python -m compileall base64_tool
```

---

## Design Principles

This project follows a deliberately simple architecture.

- Small modules
- Single responsibility
- Pure functions
- Explicit exceptions
- Readable code
- Comprehensive tests
- Incremental evolution
- Long-term maintainability

---

## Project Motto

> Simple enough to read in one sitting.
>
> Elegant enough to enjoy reading.
>
> Maintainable enough to evolve for years.

---

## Roadmap

Future releases may include:

- File encoding and decoding
- Clipboard support
- Better CLI ergonomics
- Additional output formats
- Coverage reporting
- Continuous Integration improvements

---

## Contributing

Contributions are welcome.

Please open an issue before proposing significant changes.

---

## License

Released under the MIT License.
