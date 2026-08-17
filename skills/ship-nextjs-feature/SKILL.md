---
name: ship-nextjs-feature
description: Deliver an end-to-end feature in an existing Next.js App Router application, including UI, server logic, data access, caching, accessibility, and verification. Use for feature work or substantial behavior changes in Next.js; do not use for isolated styling tweaks, Pages Router-only projects, or framework upgrades.
---

# Ship a Next.js Feature

Deliver a complete, repository-aligned feature with evidence that its user path works.

## Establish the contract

Before editing:

1. Restate the user-visible outcome and acceptance criteria.
2. Identify the affected route, layout, loading state, error state, and data boundary.
3. Inspect package scripts, Next.js configuration, TypeScript settings, tests, lint rules, and repository guidance.
4. Trace one comparable feature from route entry to persistence or external API.
5. Record unresolved product or security decisions; ask only when they materially change behavior.

Preserve the existing router, styling system, component library, data layer, authentication model, and test conventions unless the task explicitly changes them.

## Choose the execution boundary

- Default to Server Components for rendering and server-side data access.
- Add a Client Component only where browser state, effects, event handlers, or client-only APIs are required.
- Keep the client boundary small; pass serializable values across it.
- Use Server Actions for mutations tied closely to the React interaction model when the repository already uses them.
- Use Route Handlers for public HTTP interfaces, webhooks, downloads, or clients outside the React tree.
- Keep secrets, privileged SDKs, and trusted authorization checks on the server.

## Implement the vertical slice

1. Define or update domain types and validation at the trust boundary.
2. Implement authorization before privileged reads or writes.
3. Add data access using the project's established abstraction and transaction pattern.
4. Add the server operation with explicit success and expected-failure results.
5. Build the route and UI states: initial, loading, empty, success, validation error, operational error, and disabled or pending mutation.
6. Revalidate or update cached data using the narrowest mechanism already supported by the project.
7. Keep URL state shareable for filters, search, pagination, and tabs when practical.
8. Add telemetry only through existing logging or analytics facilities; do not leak personal or secret data.

## Maintain interface quality

- Reuse existing primitives before creating components.
- Preserve semantic HTML, keyboard navigation, focus behavior, labels, and readable error messages.
- Prevent duplicate submissions and make pending work visible.
- Avoid layout shifts for predictable loading content.
- Keep responsive behavior consistent with neighboring routes.

## Guard against common failures

- Do not move server-only code into a client bundle.
- Do not trust hidden fields, route parameters, cookies, or client-side role checks.
- Do not use broad cache invalidation when a path or tag can be targeted.
- Do not introduce a second fetching or form library for one feature.
- Do not suppress hydration, type, lint, or accessibility errors to finish faster.
- Do not change rendering mode globally to solve a local problem.

## Verify progressively

Run the repository's own commands, starting narrow:

1. Type-check or compile the affected package.
2. Run focused unit and component tests.
3. Run linting on changed files or the package.
4. Exercise the full route in a browser, including unauthenticated and unauthorized behavior where relevant.
5. Test one failure path and one empty state.
6. Run the production build when routing, server/client boundaries, environment access, or caching changed.

If a check cannot run, state the exact reason and the missing confidence it leaves.

## Hand off

Report:

- the completed user path;
- important server/client, authorization, and cache decisions;
- validation commands and their results;
- migrations or environment variables required;
- remaining risks or intentionally deferred work.
