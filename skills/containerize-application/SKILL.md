---
name: containerize-application
description: Create or improve a production-minded Docker container setup for an application, including build context, multi-stage images, runtime identity, configuration, health, signal handling, local orchestration, and verification. Use for Dockerfiles and Compose delivery; do not use for Kubernetes design or merely explaining container concepts.
---

# Containerize an Application

Produce a small, reproducible, non-root image that starts correctly and fits the application's deployment model.

## Inspect the runtime

1. Read repository guidance, dependency manifests and locks, build scripts, runtime version files, generated artifacts, and current deployment configuration.
2. Identify the actual production start command, listening address and port, writable paths, native system dependencies, and shutdown behavior.
3. Determine which build-time values are public and which runtime values are secret.
4. Inspect any existing Dockerfile, compose files, ignore rules, CI builds, and registry requirements.
5. Confirm target CPU architectures and whether the runtime needs a full distribution, slim image, distroless image, or special certificates and locale data.

## Design the image

- Pin a supported base image at least to a stable version; use a digest when repository policy requires reproducibility.
- Use multiple stages to separate dependency resolution, compilation, and runtime files.
- Copy dependency manifests before source so dependency layers can be cached.
- Use the project's lockfile and frozen or reproducible install mode.
- Keep compilers, package managers, test data, and source out of the runtime stage unless required.
- Create an unprivileged runtime user and ensure only required paths are writable.
- Add a narrow .dockerignore that excludes secrets, VCS data, local dependencies, test output, and unrelated artifacts.

## Configure runtime behavior

1. Bind the service to the container interface rather than loopback only.
2. Read environment-specific configuration at runtime.
3. Do not bake credentials or private environment files into image layers or build arguments.
4. Use exec-form ENTRYPOINT or CMD so the application receives termination signals.
5. Expose or document the intended port without treating EXPOSE as a firewall.
6. Add a meaningful health check only when the deployment platform will use it and the image has the required probe tool.
7. Define volumes only for data that must outlive the container.

## Compose local dependencies

When local multi-service orchestration is requested:

- Keep application build configuration aligned with the production image.
- Add dependency health checks and condition startup where supported.
- Use named volumes for durable local database data.
- Keep secrets out of committed compose files.
- Avoid host networking and privileged mode unless there is a demonstrated requirement.

## Guardrails

- Do not use latest tags for production images.
- Do not run the application as root by default.
- Do not copy the whole repository before dependency installation without a reason.
- Do not put SSH keys, cloud tokens, npm credentials, or .env files in the build context.
- Do not add curl solely for a health check without weighing its runtime cost and exposure.
- Do not claim a smaller image is safer without checking included packages and runtime needs.

## Verify

1. Build from a clean context with the same command CI will use.
2. Inspect image history and contents for secrets and unintended files.
3. Run as the configured non-root user with a read-only root filesystem where practical.
4. Start the container with representative runtime configuration and call its readiness or primary endpoint.
5. Send a termination signal and verify graceful shutdown.
6. Rebuild to observe dependency-layer caching.
7. Run the repository's image scanner when available and address actionable high-severity findings.
8. Test the declared architecture or multi-platform build when required.

## Hand off

Report the build and run commands, image stages and runtime user, ports and writable paths, required runtime variables, health and shutdown behavior, validation results, and remaining base-image or native-library risks.
