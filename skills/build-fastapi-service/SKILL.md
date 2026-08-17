---
name: build-fastapi-service
description: Implement or extend a typed FastAPI service capability with Pydantic validation, dependency boundaries, persistence, authorization, error handling, observability, and tests. Use for FastAPI routes and backend features; do not use for notebooks, generic Python automation, or replacing the project's established architecture.
---

# Build a FastAPI Service Capability

Deliver a typed vertical slice while preserving the repository's Python and service conventions.

## Inspect before editing

1. Read project guidance, dependency configuration, Python version, formatter, linter, type checker, and test commands.
2. Inspect application creation, router registration, dependency providers, exception handlers, middleware, settings, and lifespan hooks.
3. Trace a comparable endpoint through schemas, service logic, persistence, and tests.
4. Determine whether database and outbound clients are synchronous or asynchronous.
5. Identify the authentication principal, authorization rule, transaction boundary, and public compatibility requirements.

## Shape the contract

- Define separate input, update, internal, and response models when their trust or visibility differs.
- Use Pydantic constraints for syntax and simple invariants; keep database-dependent business rules in the service layer.
- Make optional, nullable, and omitted fields intentionally different.
- Set explicit status codes and response models.
- Preserve established aliasing, serialization, pagination, and error-envelope conventions.

## Implement the request path

1. Add the route to the owning router with a stable path and operation identifier if the project uses one.
2. Resolve authentication, settings, database sessions, and clients through existing dependencies.
3. Keep transport parsing in the route and business decisions in the existing service or domain layer.
4. Use the established data-access pattern; avoid leaking ORM objects after a session closes.
5. Commit or roll back at the repository's chosen transaction boundary.
6. Convert expected domain outcomes into precise HTTP errors through the project's handler pattern.
7. Record operational context through structured logging without sensitive data.

## Respect concurrency

- Do not call blocking database or network libraries directly from an async route.
- Do not make synchronous code async without an actual awaitable dependency.
- Preserve cancellation and timeouts for outbound operations.
- Scope database sessions and mutable request state per request.
- Use background tasks only for short, non-critical work; use durable infrastructure for work that must survive process loss.

## Guardrails

- Do not treat generated OpenAPI documentation as proof that authorization is correct.
- Do not return internal exception text, secrets, database URLs, or raw validation internals.
- Do not weaken validation to accommodate one malformed caller.
- Do not introduce global mutable state for request-specific data.
- Do not silently change field names, nullability, or error shapes on a public endpoint.

## Verify

1. Run formatter and lint checks on the affected package.
2. Run the configured static type checker.
3. Add focused service tests and route tests using the project's test client.
4. Cover validation, authentication, authorization, not-found, conflict, and rollback behavior as applicable.
5. Verify async tests with the project's configured event-loop tooling.
6. Start the application or build its container when wiring, imports, settings, or lifespan behavior changed.
7. Inspect the generated OpenAPI entry if the external contract changed.

State skipped checks and their impact explicitly.

## Hand off

Report the route contract, sync or async decision, dependency and transaction boundaries, security behavior, tests run, configuration or migration changes, and residual risk.
