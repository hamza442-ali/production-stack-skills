---
name: build-dotnet-api
description: Deliver an ASP.NET Core Web API capability with explicit contracts, dependency injection, validation, authorization, EF Core persistence, problem responses, observability, and tests. Use for .NET backend feature work; do not use for desktop UI, isolated C# scripts, or unnecessary architecture replacement.
---

# Build a .NET API Capability

Implement a production-minded vertical slice that follows the solution's established ASP.NET Core style.

## Inspect the solution

1. Read repository guidance, global.json, target frameworks, solution and project files, analyzers, formatting, and test commands.
2. Inspect Program startup, configuration binding, dependency registration, middleware order, authentication, authorization policies, exception handling, OpenAPI, and health checks.
3. Trace a comparable endpoint through contract, handler or service, EF Core or other storage, and tests.
4. Identify compatibility, tenancy or ownership, transaction, cancellation, and migration requirements.

Use either controllers or minimal APIs according to the project. Do not mix styles without a clear repository precedent.

## Define the contract

- Use request and response records or DTOs rather than exposing EF entities accidentally.
- Express nullability accurately and preserve JSON naming conventions.
- Validate untrusted input through the project's existing validation mechanism.
- Define stable status codes and ProblemDetails responses for expected failures.
- Update OpenAPI metadata when the project publishes a contract.

## Implement the request path

1. Keep the endpoint focused on transport concerns.
2. Put business decisions in the current application or domain boundary.
3. Register dependencies with the narrowest correct lifetime.
4. Propagate CancellationToken into EF Core and outbound asynchronous calls.
5. Use async I/O end to end; avoid sync-over-async.
6. Use tracked queries for intentional updates and no-tracking queries for read-only work when consistent with the data layer.
7. Apply a transaction around multi-step atomic changes.
8. Enforce authorization policies and resource ownership with server-trusted data.
9. Map expected failures to the established result or exception pattern.

## Operational quality

- Bind and validate configuration through Options patterns already used by the solution.
- Use ILogger structured message templates without secrets or sensitive payloads.
- Respect HttpClientFactory, resilience, and timeout conventions for outbound calls.
- Keep health checks representative without exposing internals publicly.
- Make retried commands idempotent when the caller or infrastructure may repeat them.

## Guardrails

- Do not create a service locator from IServiceProvider inside application logic.
- Do not give scoped dependencies to singleton services.
- Do not block Task results with Result, Wait, or GetAwaiter in request code.
- Do not disable nullable analysis or authorization to silence failures.
- Do not return exception messages or stack traces to clients.
- Do not edit generated migrations after they have been applied to shared environments without a deliberate repair plan.

## Verify

1. Run dotnet format or the repository's formatting check.
2. Build the affected solution with warnings treated according to repository policy.
3. Run focused unit tests, then the relevant test projects.
4. Add WebApplicationFactory or equivalent integration coverage for the public contract.
5. Cover validation, authentication, forbidden access, absence, conflict, cancellation, and transaction rollback as relevant.
6. Generate and apply EF Core migrations against a disposable database when schema changed.
7. Start the application or container when startup, configuration, middleware, or DI registrations changed.

## Hand off

Report the public contract, DI lifetime and cancellation decisions, authorization and data impact, migrations or configuration required, validation evidence, and remaining risk.
