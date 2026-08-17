---
name: review-application-security
description: Perform an evidence-based defensive security review of an application change or repository, prioritizing exploitable trust-boundary failures and producing actionable findings with verification guidance. Use for authorized code security reviews and threat-focused assessments; do not use for offensive intrusion, credential harvesting, or claims of compliance certification.
---

# Review Application Security

Find credible, actionable security problems in authorized code and explain them with enough evidence to reproduce and fix safely.

## Set scope and threat model

1. Confirm the repository, change, feature, or data flow in scope.
2. Identify exposed entry points, trusted and untrusted actors, sensitive assets, privilege levels, and external dependencies.
3. Map trust boundaries across browser, API, background work, database, filesystem, cloud services, and administrative paths.
4. Read repository guidance and existing security, authentication, tenancy, secret-management, and logging conventions.
5. Trace the actual code path before forming a finding.

For pull requests, focus first on security behavior introduced or changed by the diff, then inspect adjacent code needed to establish exploitability.

## Review high-value categories

Prioritize:

- authentication, session lifecycle, token validation, and account recovery;
- authorization, object ownership, tenancy isolation, and administrative actions;
- injection into SQL, shells, templates, paths, URLs, headers, and interpreters;
- server-side request forgery and unsafe redirects;
- unsafe file upload, download, extraction, and content handling;
- secret exposure through source, client bundles, logs, errors, artifacts, or configuration;
- cryptographic misuse and insecure randomness;
- deserialization, parser, and resource-exhaustion risks;
- cross-site scripting, request forgery, CORS, clickjacking, and browser storage;
- webhook verification, replay protection, race conditions, and idempotency;
- dependency or workflow changes that materially expand execution trust.

## Establish a finding

Report a security finding only when evidence connects:

1. an attacker-controlled source;
2. a reachable code path;
3. a missing or ineffective control;
4. a meaningful security impact.

Check for upstream validation, framework defaults, middleware, database constraints, network policy, and deployment configuration that may block the path. Distinguish confirmed findings from defense-in-depth suggestions and unresolved questions.

## Write actionable findings

For each confirmed issue include:

- concise title and severity with rationale;
- affected file and the smallest useful location;
- attacker prerequisites and controlled input;
- execution path and impact;
- why existing controls do not stop it;
- a safe remediation aligned with repository architecture;
- a focused regression test or verification procedure.

Avoid inflated severity. Use likelihood, reachability, privilege gained, data sensitivity, blast radius, and recovery difficulty.

## Guardrails

- Review only systems and code the user is authorized to assess.
- Do not retrieve real credentials, access unrelated data, establish persistence, or perform destructive proof-of-concept actions.
- Use synthetic inputs and local or disposable environments for dynamic verification.
- Do not publish secrets or unnecessarily reproduce sensitive values in the report.
- Do not label stylistic quality, generic hardening, or missing best practices as vulnerabilities without a credible impact path.
- Do not claim the review proves the absence of vulnerabilities or certifies compliance.

## Verify

1. Use static tracing and repository search to follow sources, transformations, controls, and sinks.
2. Run focused existing tests and safe security checks.
3. Add a non-destructive regression test when fixing an issue is in scope.
4. Confirm the proposed fix closes the path without relying only on client controls.
5. Recheck adjacent variants of the same pattern.
6. Record areas not reviewed and dynamic checks blocked by unavailable infrastructure.

## Hand off

Lead with confirmed findings ordered by severity. Then list unresolved questions, defense-in-depth improvements separately, checks performed, scope limitations, and a concise overall risk statement. If no findings are confirmed, say so and describe the remaining blind spots.
