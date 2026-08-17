---
name: build-nestjs-api
description: Add or change a production HTTP API capability in an existing NestJS application, covering modules, DTO validation, services, persistence, authorization, errors, documentation, and tests. Use for NestJS endpoint and domain work; do not use for generic Node scripts, frontend work, or a wholesale architecture rewrite.
---

# Build a NestJS API Capability

Implement a cohesive API slice that follows the application's established NestJS architecture.

## Inspect the service

1. Read repository guidance, package scripts, TypeScript settings, bootstrap code, and global pipes, filters, guards, and interceptors.
2. Locate the owning module and trace a comparable request through controller, service or use case, repository, and database.
3. Identify the public contract, authentication scheme, authorization rules, transaction needs, and compatibility constraints.
4. Confirm how configuration, logging, API documentation, migrations, and tests are handled.

Do not add a new architectural layer merely because a preferred pattern differs from the repository.

## Define the API contract

- Choose the HTTP method and route from resource semantics, not implementation convenience.
- Model request DTOs with explicit validation and transformation rules.
- Keep response DTOs stable and prevent persistence models from leaking accidentally.
- Define status codes for success, creation, absence, conflicts, validation failures, and authorization failures.
- Preserve existing versioning and serialization conventions.
- Update OpenAPI decorators or generated contract sources when the project maintains API documentation.

## Implement through the module boundary

1. Add the controller method as a thin transport adapter.
2. Put business rules and orchestration in the existing service or use-case layer.
3. Use dependency injection tokens and module exports intentionally.
4. Keep database queries in the established repository or ORM boundary.
5. Use a transaction when multiple writes must succeed or fail together.
6. Translate expected domain failures into the project's exception or result pattern.
7. Add guards or policy checks at the layer used by the codebase; verify resource ownership in trusted server code.
8. Emit structured logs for operational failures without recording tokens, passwords, or sensitive payloads.

## Handle asynchronous behavior

- Await promises at the correct boundary and preserve useful error context.
- Use queues or events only when the project already supports them and the operation can be eventually consistent.
- Make externally retried mutations idempotent when duplicate execution is plausible.
- Apply timeouts and cancellation through existing infrastructure for outbound calls.

## Guardrails

- Do not rely on TypeScript types as runtime validation.
- Do not return raw ORM entities by default.
- Do not catch every error and convert it to a generic success or 500 response.
- Do not create circular module dependencies to avoid designing a clear ownership boundary.
- Do not bypass global validation, authentication, tenancy, or serialization behavior.
- Do not change a public response shape without calling out compatibility impact.

## Verify

1. Run focused service and controller unit tests.
2. Add or update an end-to-end test for the public request and response.
3. Cover validation, unauthenticated access, forbidden access, absence, and one domain conflict as applicable.
4. Run type-checking, linting, and the relevant package build.
5. Apply migrations in a disposable or test database if persistence changed.
6. Confirm generated OpenAPI output or route registration when the project supports it.

Use the repository's scripts. Never claim a database or end-to-end check passed if infrastructure was unavailable.

## Hand off

Summarize the API contract, module ownership, authorization rule, persistence and migration impact, checks run, and any rollout or compatibility concern.
