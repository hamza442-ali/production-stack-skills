---
name: build-spring-boot-api
description: Deliver a production Spring Boot REST API change with validated contracts, service and transaction boundaries, persistence, authorization, structured errors, migrations, and tests. Use for Spring Boot backend features; do not use for Android, plain Java utilities, or replacing established project architecture.
---

# Build a Spring Boot API

Deliver a cohesive API change that respects the application's current Spring conventions.

## Inspect the application

1. Read repository guidance, Java and Spring Boot versions, build files, profiles, formatting, static analysis, and test setup.
2. Inspect application configuration, security chains, exception advice, controller patterns, persistence strategy, migration tooling, and observability.
3. Trace a comparable endpoint through controller, service, repository, mapping, and tests.
4. Identify contract compatibility, authentication principal, resource authorization, transaction needs, and database constraints.

Follow the project's choice of MVC or WebFlux. Do not mix blocking persistence into a reactive request path.

## Define the contract

- Use dedicated request and response records or DTOs when entity exposure would couple the API to persistence.
- Apply Jakarta validation to request syntax and simple invariants.
- Keep domain and database-dependent rules in the service layer.
- Choose precise HTTP status codes and preserve existing error-envelope and versioning conventions.
- Document the contract through the project's OpenAPI mechanism when present.

## Implement by responsibility

1. Keep controllers thin: bind, validate, authorize at the established boundary, invoke, and map the result.
2. Place orchestration and business rules in the owning service.
3. Define transaction boundaries around complete business operations, not individual repository calls.
4. Use repositories and query methods that avoid accidental unbounded reads and N+1 behavior.
5. Map entities deliberately and avoid lazy-loading surprises during serialization.
6. Enforce resource ownership or policy with trusted data.
7. Convert expected domain failures through the existing ControllerAdvice or exception hierarchy.
8. Add migrations for schema changes; do not rely on automatic production schema mutation.

## Operational quality

- Keep configuration external and typed where the project supports ConfigurationProperties.
- Use structured, parameterized logging and omit credentials or sensitive payloads.
- Apply existing timeouts, retries, and circuit breakers to outbound calls.
- Preserve actuator health and readiness behavior.
- Consider idempotency for endpoints likely to be retried.

## Guardrails

- Do not return JPA entities directly unless the project deliberately treats them as the API contract.
- Do not place transactional annotations on private methods or assume self-invocation creates a proxy boundary.
- Do not disable CSRF, authentication, or method security to make a test pass.
- Do not catch Exception broadly and erase the cause.
- Do not introduce both reactive and servlet stacks unintentionally.

## Verify

1. Run focused unit tests for service rules.
2. Run controller slice or WebTestClient tests for the HTTP contract.
3. Add integration tests for persistence, transactions, authorization, and migrations as applicable.
4. Cover invalid input, unauthenticated, forbidden, not-found, conflict, and rollback paths.
5. Run the repository's formatter, static analysis, test, and build tasks.
6. Start the packaged application or container when configuration, wiring, security, or migrations changed.

## Hand off

Report the endpoint contract, transaction and authorization boundaries, persistence impact, migration and configuration requirements, commands run, and rollout risks.
