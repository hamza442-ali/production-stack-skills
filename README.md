# Production Stack Skills

Original, production-oriented Agent Skills for common software stacks. Each skill gives a coding agent a focused operating procedure: how to inspect a codebase, make safe decisions, implement a change, verify it, and report the result.

These skills are written from first principles. They are not copies of vendor guides or other skill collections.

## What “installing a skill” means

Installing a skill makes its `SKILL.md` available in an agent's configured skills directory so the agent can discover and follow it. It does **not** install Node.js, Go, Docker, a framework, packages, or cloud credentials.

## Included skills

| Skill | Purpose |
| --- | --- |
| `ship-nextjs-feature` | Deliver a complete feature in a Next.js App Router application |
| `build-nestjs-api` | Add or change a production NestJS HTTP API capability |
| `build-fastapi-service` | Implement a typed FastAPI service capability |
| `build-go-service` | Build or extend an idiomatic Go HTTP service |
| `build-spring-boot-api` | Deliver a Spring Boot REST API change |
| `build-dotnet-api` | Deliver an ASP.NET Core Web API change |
| `design-postgres-schema` | Design and migrate a PostgreSQL schema safely |
| `build-flutter-feature` | Implement a complete Flutter application feature |
| `containerize-application` | Create a production-minded container setup |
| `deploy-vercel-application` | Prepare and verify an application for Vercel |
| `build-github-actions-ci` | Create maintainable GitHub Actions CI workflows |
| `review-application-security` | Perform an evidence-based application security review |

## Install

Copy a complete skill directory into the skills directory used by your agent. Preserve `SKILL.md`, `agents/openai.yaml`, and any referenced files together.

Example for a local Codex setup:

```bash
cp -R skills/ship-nextjs-feature ~/.codex/skills/
```

Restart or open a fresh agent session if the agent does not discover newly installed skills immediately. Exact skill locations vary by agent, so check that agent's documentation.

## Use

Ask naturally, or invoke a skill explicitly when the client supports it:

```text
Use $ship-nextjs-feature to add account deletion to this application.
```

The agent should still inspect and respect the repository's existing conventions. A skill supplies a workflow and quality bar, not permission to replace a project's architecture.

## Design principles

- One focused job per skill.
- Triggering and exclusions are clear in the description.
- Inspect before changing; preserve local conventions by default.
- Treat validation, migrations, secrets, and destructive actions explicitly.
- Verify the smallest relevant checks first, then broaden confidence.
- Report evidence, residual risks, and follow-up work honestly.
- Keep core instructions compact; move deep details into references only when needed.

## Repository layout

```text
skills/<skill-name>/
├── SKILL.md
└── agents/
    └── openai.yaml
```

## Contributing

Run the validator before committing:

```bash
python3 scripts/validate_skills.py
```

Keep each skill change in a focused commit and avoid combining unrelated skill revisions.

## License

MIT
