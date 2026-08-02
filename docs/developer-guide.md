# Developer Guide

## Philosophy

The project intentionally favors readability over cleverness.

Every module should have a single responsibility.

Every function should be easy to understand in one reading.

Business logic should remain independent from user interaction.

## Project Structure

The project is organized as follows.

```text
base64_tool/
    codec.py
    validator.py
    interactive.py
    cli.py
    exceptions.py
```

Each module owns one responsibility.

## Development Workflow

For every modification:

1. Implement the change.
2. Compile the project.
3. Run the complete test suite.
4. Review the diff.
5. Commit a single logical change.

## Testing

Run the complete test suite.

```bash
python -m pytest
```

Compile every Python module.

```bash
python -m compileall base64_tool
```

## Style

The project follows these principles.

- Small modules
- Small functions
- Explicit exceptions
- Pure business logic
- Comprehensive unit tests

## Versioning

The project follows Semantic Versioning.

