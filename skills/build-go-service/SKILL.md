---
name: build-go-service
description: Build or extend an idiomatic Go HTTP service capability with clear package ownership, context propagation, validation, persistence, concurrency safety, observability, and tests. Use for Go backend feature work; do not use for tiny standalone utilities, non-Go services, or unnecessary framework replacement.
---

# Build a Go Service Capability

Implement a small, composable vertical slice that fits the service's current package design.

## Inspect the codebase

1. Read repository guidance, go.mod, toolchain version, build targets, lint configuration, and test commands.
2. Locate process startup, configuration loading, router registration, middleware, graceful shutdown, logging, and health checks.
3. Trace a similar handler through domain or service logic, storage, and tests.
4. Identify public compatibility, authorization, transaction, timeout, and concurrency requirements.
5. Confirm whether generated code is present and how it must be regenerated.

Prefer the standard library and existing dependencies. A feature is not a reason to introduce a new router, dependency-injection system, logger, or assertion library.

## Design the boundary

- Keep HTTP parsing and response encoding in handlers.
- Express domain behavior through small concrete types and interfaces owned by the consumer.
- Accept context.Context as the first parameter for request-scoped I/O; do not store it on structs.
- Validate untrusted input at the transport boundary and enforce business invariants in domain logic.
- Preserve existing JSON field names, error envelopes, and status-code conventions.

## Implement the slice

1. Add or extend the smallest owning package.
2. Wire dependencies explicitly at process startup.
3. Propagate request context into database and outbound calls.
4. Wrap errors with operation context while preserving errors.Is or errors.As behavior.
5. Map expected errors to stable HTTP responses; log unexpected errors once at an operational boundary.
6. Use database transactions only around the atomic unit of work.
7. Close response bodies, rows, files, and other owned resources predictably.
8. Make retried writes idempotent when duplicates are plausible.

## Concurrency and lifecycle rules

- Share mutable state only with a clear synchronization strategy.
- Prefer ownership through goroutines and channels when that clarifies lifecycle; otherwise use a mutex directly.
- Never start an unbounded goroutine per item or leave a goroutine without cancellation.
- Bound parallelism and queues.
- Honor server, client, and shutdown timeouts from existing configuration.
- Avoid copying types that contain mutexes.

## Guardrails

- Do not panic for ordinary request or dependency failures.
- Do not hide all failures behind one sentinel error.
- Do not add interfaces before there is a real substitution or test boundary.
- Do not log secrets, credentials, or full sensitive request bodies.
- Do not change generated files by hand.
- Do not use context.Background inside a request path to escape cancellation.

## Verify

1. Run gofmt on changed Go files.
2. Run focused tests, then go test ./... when practical.
3. Run go vet ./... and the repository's configured linter.
4. Add table-driven tests for validation and domain branches where useful.
5. Use httptest for the public handler contract.
6. Run tests with the race detector for changed concurrent code.
7. Build the service binary or container and exercise graceful startup and shutdown when wiring changed.

Report environment-dependent checks honestly.

## Hand off

Summarize package ownership, public behavior, error and context handling, concurrency decisions, validation evidence, operational changes, and remaining risk.
