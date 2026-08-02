# ADR 0002 - Error Handling

## Status

Accepted

## Context

Errors should communicate domain failures without exposing
implementation details.

## Decision

Introduce a dedicated exception hierarchy rooted at
`Base64ToolError`.

## Consequences

Applications may safely catch one base exception.

Future exceptions can be added without breaking the API.

