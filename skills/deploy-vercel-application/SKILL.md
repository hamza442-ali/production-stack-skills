---
name: deploy-vercel-application
description: Prepare, configure, deploy, and verify an application on Vercel with correct project linkage, build settings, runtime choices, environment variables, domains, observability, and rollback awareness. Use for Vercel delivery and deployment failures; do not use for unrelated hosting providers or feature development with no deployment impact.
---

# Deploy a Vercel Application

Make the repository deployable on Vercel and verify the resulting application rather than stopping at a successful build log.

## Establish deployment context

1. Read repository guidance, framework configuration, package-manager lockfile, monorepo structure, build commands, output paths, runtime declarations, and existing Vercel files.
2. Determine whether the repository is already linked to a Vercel project. Preserve the existing project unless the user explicitly requests a new one.
3. Identify production, preview, and development environment differences.
4. Inventory required environment variable names and classify them as public or server-only; never print secret values.
5. Identify serverless, edge, static, image, cron, routing, storage, and domain requirements.
6. Reproduce the production build locally when practical before changing platform settings.

Use the project's configured Vercel integration, command-line tool, or connected API. Treat project and deployment identifiers as opaque values.

## Prepare the application

- Keep the correct workspace root and package manager for monorepos.
- Pin runtime versions using repository-supported configuration.
- Ensure build-time variables are available only where needed and runtime secrets remain server-side.
- Choose Node.js, Edge, or static execution per route capability; do not move incompatible libraries to Edge.
- Make filesystem assumptions explicit because deployed functions have ephemeral local storage.
- Configure rewrites, redirects, headers, functions, and cron jobs in the narrowest supported file or framework layer.
- Preserve preview isolation for databases, webhooks, and third-party callbacks when the application supports it.

## Deploy safely

1. Link or select the exact project and team.
2. Synchronize variable names across the correct environments without exposing values in logs or commits.
3. Create a preview deployment first for meaningful changes.
4. Record the source commit associated with the deployment.
5. Inspect build output, function bundling, route configuration, and warnings.
6. Promote or create a production deployment only after preview verification, unless the user explicitly requests a direct production release.
7. Keep the previous healthy deployment available for rollback.

## Verify the real user path

- Wait for a terminal deployment state.
- Open the deployed URL and exercise the primary route.
- Test one dynamic or authenticated path when relevant.
- Verify API or server action behavior and its backing data.
- Check browser console, runtime logs, and failed network requests.
- Confirm asset, image, cache, redirect, and custom-domain behavior affected by the change.
- Verify scheduled or webhook behavior with safe test events when applicable.

## Guardrails

- Do not create duplicate Vercel projects because linkage is missing locally.
- Do not commit .vercel credentials, tokens, or populated environment files.
- Do not expose secrets through public-prefixed variables.
- Do not describe a deployment as successful before both platform status and an application check pass.
- Do not change DNS, production aliases, or domains outside the explicit request.
- Do not paper over build errors by disabling type or lint checks globally.

## Hand off

Report the project and environment targeted, source commit, deployment URL and final status, configuration changes, user paths verified, logs or checks inspected, and the rollback or remaining-risk note. Never include secret values.
