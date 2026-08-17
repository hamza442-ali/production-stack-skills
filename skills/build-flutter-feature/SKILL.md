---
name: build-flutter-feature
description: Implement a complete Flutter feature across presentation, state, domain, data, navigation, accessibility, platform behavior, and tests. Use for substantial Flutter app features or behavior changes; do not use for native-only iOS or Android work, isolated visual polish, or replacing the app's state architecture.
---

# Build a Flutter Feature

Deliver a complete user flow that fits the application's current architecture and works across its supported platforms.

## Inspect the application

1. Read repository guidance, pubspec, Dart and Flutter constraints, analysis options, flavors, code generation, and test commands.
2. Inspect app startup, dependency injection, navigation, theming, localization, state management, networking, persistence, analytics, and error reporting.
3. Trace a comparable feature from route and widgets through state, domain logic, repository, and tests.
4. Identify target platforms, offline expectations, permissions, deep links, and backward-compatible data concerns.

Reuse the existing state-management and navigation approach. A single feature is not justification for adding a competing framework.

## Define the feature contract

- State the entry point, happy path, empty state, loading state, retry behavior, validation errors, and completion behavior.
- Identify which state is ephemeral widget state, shared application state, persisted state, or server-owned state.
- Define domain models separately from API payloads when their lifecycles differ.
- Confirm navigation arguments and result behavior, including deep-link restoration when applicable.

## Implement in layers

1. Add or update data transfer models and explicit mapping at the API or storage boundary.
2. Implement repository behavior using existing clients, authentication, caching, and error translation.
3. Keep business decisions in the project's domain or state layer rather than widgets.
4. Model state transitions explicitly so stale success data and new errors do not combine accidentally.
5. Build small widgets with stable keys where tests or state preservation need them.
6. Integrate navigation, localization, analytics, and permissions through existing services.
7. Handle disposal, cancellation, subscriptions, controllers, and mounted checks according to ownership.

## Interface quality

- Use theme and design-system tokens rather than isolated constants.
- Provide semantic labels, logical focus order, sufficient touch targets, text scaling, and screen-reader feedback.
- Preserve keyboard and back behavior on supported platforms.
- Avoid expensive work in build methods.
- Use lazy lists for unbounded content and constrain images appropriately.
- Make optimistic updates reversible when the server can reject them.

## Guardrails

- Do not call repositories directly from leaf widgets if the application has a state boundary.
- Do not retain BuildContext across asynchronous gaps without a safe mounted check.
- Do not ignore platform-specific permission denial or permanent denial.
- Do not regenerate or hand-edit generated files inconsistently.
- Do not log access tokens, personal data, or full sensitive responses.
- Do not add broad keep-alive behavior to hide incorrect state ownership.

## Verify

1. Run dart format and flutter analyze.
2. Run focused unit tests for mapping, validation, and state transitions.
3. Add widget tests for loading, success, empty, error, retry, and accessibility-critical behavior.
4. Add integration coverage for the main user journey when project infrastructure supports it.
5. Run code generation and confirm no unexpected diff.
6. Build or launch on each materially affected platform; test small and large viewports, text scaling, back navigation, and offline or failure behavior.

## Hand off

Report the completed flow, state and data ownership, platform considerations, generated or configuration changes, checks run, and any unverified device-specific risk.
