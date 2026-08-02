# ADR 0004 - Command-Line Interface

## Status

Accepted

## Context

The project should support both scripting and interactive use.

## Decision

Implement the CLI with `argparse`.

Interactive mode remains independent from command-line parsing.

## Consequences

The CLI is simple.

Automation is straightforward.

Future commands can be added without redesigning the interface.

