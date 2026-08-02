# ADR 0003 - Module Boundaries

## Status

Accepted

## Context

Mixing business logic and user interaction complicates testing.

## Decision

Keep encoding, validation, CLI and interactive mode in separate
modules.

## Consequences

Business logic remains reusable.

The command-line interface stays thin.

Unit testing becomes straightforward.

