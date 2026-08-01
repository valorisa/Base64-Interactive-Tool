# Contributing

Thank you for your interest in Base64 Interactive Tool.

Contributions of all sizes are welcome, whether they improve the code,
documentation or the overall developer experience.

## Philosophy

This project intentionally remains small.

Every contribution should preserve the following qualities:

- simplicity;
- readability;
- maintainability;
- testability;
- explicit behavior.

Whenever several solutions are possible, prefer the simplest one that remains
clear.

## Project Principles

The project follows a few simple architectural rules.

- One module, one responsibility.
- Small functions are preferred.
- Pure business logic remains independent from the user interface.
- Exceptions should always be explicit.
- Public APIs should remain stable whenever practical.

## Coding Style

Please keep the code consistent with the existing style.

General recommendations:

- Follow PEP 8.
- Use descriptive names.
- Avoid unnecessary abstractions.
- Keep modules reasonably small.
- Document public functions with docstrings.

As general guidelines:

- Modules should ideally stay below 200 lines.
- Functions should ideally stay below 20 lines.
- Exceptionally, a function may reach about 30 lines when justified.

## Testing

Every new feature should include tests whenever practical.

Before opening a Pull Request, run:

```bash
python -m pytest
python -m compileall base64_tool
```

The test suite should remain green.

## Commits

Small and focused commits are preferred.

The project follows the Conventional Commits specification whenever practical.

Examples:

```text
feat(cli): add clipboard support

fix(codec): reject invalid padding

refactor(validator): simplify validation logic

docs: improve installation instructions
```

## Pull Requests

A good Pull Request should:

- solve one problem;
- remain easy to review;
- include tests when appropriate;
- update the documentation if needed.

Large Pull Requests are discouraged.

## Reporting Issues

When reporting a bug, please include:

- Python version;
- Operating system.
- Command executed.
- Expected behavior.
- Observed behavior.
- Steps to reproduce the issue.

A minimal reproducible example is always appreciated.

## Questions

Questions, suggestions and constructive discussions are always welcome.

## Project Motto

> Simple enough to read in one sitting.
>
> Elegant enough to enjoy reading.
>
> Maintainable enough to evolve for years.
