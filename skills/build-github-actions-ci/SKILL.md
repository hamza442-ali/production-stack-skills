---
name: build-github-actions-ci
description: Create or improve maintainable GitHub Actions continuous integration for a software repository, covering triggers, permissions, dependency caching, matrices, artifacts, concurrency, secrets, and verification. Use for CI workflow delivery; do not use for application deployment pipelines unless deployment is explicitly part of the request.
---

# Build GitHub Actions CI

Create a least-privilege workflow that gives fast, reproducible, actionable feedback on repository changes.

## Inspect the repository

1. Read repository guidance, existing workflows, required checks, branch strategy, package manifests, lockfiles, runtime version files, and local validation commands.
2. Identify monorepo packages, generated code, service dependencies, integration tests, and platform-specific requirements.
3. Determine events that should run CI: pull requests, pushes to protected branches, merge queue, or manual dispatch.
4. Confirm whether contributions can originate from forks and which steps would require secrets.
5. Reuse existing action versions, naming, caching, and security policies where sound.

CI should run the same trusted commands developers use locally. Do not invent a second build system inside YAML.

## Design the workflow

- Give workflows and jobs stable, descriptive names suitable for required checks.
- Set explicit permissions at workflow or job scope, starting with contents: read.
- Use concurrency groups to cancel superseded pull-request runs while preserving important branch runs.
- Pin runner operating systems and language versions deliberately.
- Use a matrix only when supported versions or platforms genuinely need independent coverage.
- Separate fast static checks from slower integration checks when it improves feedback and required-check clarity.
- Add path filters cautiously; required jobs must not disappear in a way that blocks merging.

## Implement reproducibly

1. Check out the exact triggering commit.
2. Set up the runtime using official or repository-approved actions.
3. Restore caches keyed by operating system, runtime, and lockfile content; never treat caches as required correctness.
4. Install dependencies using the lockfile's frozen mode.
5. Run formatting checks, linting, type checks, tests, and build steps in the repository's intended order.
6. Start service containers or provision disposable infrastructure only for jobs that need them.
7. Upload small, useful artifacts such as test reports or coverage when a failure would otherwise be hard to diagnose.
8. Apply explicit timeouts to jobs likely to hang.

## Protect secrets and supply chain

- Do not expose secrets to untrusted pull-request code.
- Do not use pull_request_target to execute checked-out contributor code.
- Prefer short-lived identity federation over long-lived cloud credentials.
- Pin third-party actions to a full commit SHA when repository policy requires strong supply-chain control; record the human-readable version in a comment.
- Keep write permissions and tokens out of ordinary validation jobs.
- Avoid printing contexts or environment data that may contain credentials.

## Guardrails

- Do not add continue-on-error to required correctness checks without an explicit policy decision.
- Do not hide flaky tests behind retries without tracking the defect.
- Do not upload dependency directories as artifacts when caching is appropriate.
- Do not duplicate jobs when reusable workflows or composite actions already own the behavior.
- Do not add deployment, release, or repository mutation to CI unless explicitly requested.

## Verify

1. Parse the YAML and inspect the rendered workflow in GitHub.
2. Run all underlying commands locally where practical.
3. Trigger the workflow on a branch or pull request and wait for terminal job states.
4. Inspect logs for cache behavior, warnings, deprecations, and accidental secret output.
5. Confirm failure reporting by reasoning through or safely exercising a failing command.
6. Verify required-check names, fork behavior, concurrency cancellation, and artifact retention.

## Hand off

Report triggers, jobs, permissions, cache keys, required secrets by name only, commands run, observed workflow results, and any branch-protection or follow-up configuration the repository owner must apply.
