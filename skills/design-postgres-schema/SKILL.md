---
name: design-postgres-schema
description: Design and migrate a PostgreSQL schema safely, including data modeling, constraints, indexes, compatibility, backfills, locking risk, rollback strategy, and verification. Use for production database schema changes and query-driven modeling; do not use for routine data edits, non-PostgreSQL databases, or ORM-only changes with no schema impact.
---

# Design a PostgreSQL Schema

Produce a schema and rollout plan that protect integrity, availability, and application compatibility.

## Gather evidence

1. Inspect existing migrations, schema, extensions, naming conventions, ORM models, query code, and deployment process.
2. Identify PostgreSQL version and managed-service restrictions.
3. Describe the entities, relationships, lifecycle, ownership, retention, and expected scale.
4. Collect the important read and write access patterns, including filters, joins, ordering, uniqueness, and concurrency.
5. Determine whether the change must support old and new application versions simultaneously.
6. Estimate table size and traffic before choosing operations that rewrite data or acquire strong locks.

Do not design from entity names alone. Queries and invariants determine a useful production schema.

## Model integrity

- Choose types that represent the domain without ambiguous sentinel values.
- Use NOT NULL when absence is invalid.
- Encode uniqueness, referential integrity, and simple invariants as database constraints.
- Define foreign-key delete behavior deliberately.
- Prefer generated identity or repository conventions for keys; do not change key strategy casually.
- Store timestamps with a clear timezone policy and use database defaults only when ownership is explicit.
- Use JSONB for genuinely variable or document-shaped attributes, not to avoid modeling stable relational data.
- Avoid PostgreSQL enum types when values must change frequently unless the repository has a safe enum migration strategy.

## Design indexes from queries

1. Start with real predicates, join keys, sort order, and selectivity.
2. Order composite index columns to serve the target access pattern.
3. Use partial indexes for stable predicates that exclude much of a table.
4. Use expression indexes only when queries use the same expression.
5. Consider covering columns when they materially reduce heap access.
6. Check whether an existing index already satisfies the query.

Every index adds write and storage cost. Do not add speculative indexes for every column or foreign key without examining access patterns.

## Plan an online migration

Use an expand-migrate-contract sequence for compatibility-sensitive changes:

1. Expand with additive, nullable, or parallel structures.
2. Deploy code that can read and write across the transition.
3. Backfill in bounded, restartable batches with observable progress.
4. Validate constraints using the least-blocking supported technique.
5. Switch reads after data and metrics confirm readiness.
6. Enforce stricter constraints and remove obsolete structures only after old code is gone.

Separate transaction-incompatible statements when required. Use concurrent index operations for large live tables when supported by the deployment tooling. Set deliberate lock and statement timeouts rather than waiting indefinitely.

## Guardrails

- Do not combine a large backfill with a schema lock in one migration.
- Do not add a volatile default or type conversion to a large table without checking rewrite behavior for the target PostgreSQL version.
- Do not drop or rename a column while deployed code may still use it.
- Do not assume down migrations can restore deleted or transformed data.
- Do not disable constraints permanently to improve write speed.
- Do not run destructive SQL against a shared environment without explicit authorization and a verified target.

## Verify

1. Apply the full migration chain to an empty disposable database.
2. Apply the new migration to a representative pre-change database.
3. Test concurrent old and new application behavior when rollout requires it.
4. Compare query plans with EXPLAIN (ANALYZE, BUFFERS) using representative data where safe.
5. Test uniqueness, nullability, foreign keys, delete behavior, and transaction conflicts.
6. Measure backfill batch duration and confirm restartability.
7. Verify rollback or roll-forward recovery steps and backup expectations.

## Hand off

Provide the target schema, supported queries, migration phases, locking and compatibility risks, backfill and recovery plan, validation evidence, and the conditions required before contract cleanup.
