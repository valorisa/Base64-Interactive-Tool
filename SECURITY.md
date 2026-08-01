# Security Policy

## Supported Versions

The latest stable release is the only version that receives security
updates.

Older releases may contain known vulnerabilities and should be upgraded
whenever possible.

| Version | Supported |
| -------- | :-------: |
| 2.x | ✅ |
| 1.x | ❌ |

## Reporting a Vulnerability

If you believe you have discovered a security vulnerability, please do not
open a public GitHub issue.

Instead, contact the project maintainer privately and provide as much
information as possible, including:

- a description of the issue;
- the affected version;
- detailed reproduction steps;
- proof of concept if applicable;
- any suggested mitigation.

## Response Process

Security reports will be acknowledged as quickly as practical.

Each report will be reviewed to determine:

- reproducibility;
- impact;
- affected versions;
- appropriate remediation.

When a vulnerability is confirmed, a fix will be prepared and released as
soon as reasonably possible.

## Responsible Disclosure

Please allow adequate time for the issue to be investigated and corrected
before making any public disclosure.

Responsible disclosure helps protect all users of the project.

## Scope

This policy applies to:

- the Python package;
- the command-line interface;
- the interactive mode;
- project documentation;
- GitHub Actions workflows.

Third-party dependencies remain subject to their own security policies.

## Security Philosophy

This project follows a few simple principles:

- keep the codebase small;
- minimize dependencies;
- prefer the Python standard library;
- write deterministic and testable code;
- review changes before merging;
- keep documentation synchronized with the implementation.

Security is considered an ongoing process rather than a one-time feature.
