# DevOps Best Practices in Git, CI and CD

## Git best practices
- protect `main`; do not commit directly to it
- use short-lived branches
- write meaningful commit messages
- keep commits small and reviewable
- review code through Pull Requests
- keep `.gitignore` clean and strict
- never commit secrets, credentials, browser artifacts, or local config
- tag releases using semantic versioning

## CI best practices
- run CI on every pull request
- lint early so failures happen fast
- keep builds deterministic with pinned dependency versions
- install only what is needed in CI
- upload reports and logs for debugging
- keep pipeline runtime reasonable
- fail the merge if CI fails

## CD best practices
- separate CI from CD
- deploy only after validated builds
- release from tags or protected branches
- publish immutable image versions
- keep `latest` as a convenience tag, not as the only deployment reference
- use environments for approval gates
- track exactly what version was deployed

## GHCR best practices
- use `ghcr.io/<owner>/<image>:<version>` style version tags
- also publish `latest` only for stable releases
- keep image metadata labels on published artifacts
- prefer repository-linked packages so permissions stay aligned

## Security best practices
- use least privilege in workflows
- use `GITHUB_TOKEN` where enough
- prefer short-lived credentials or OIDC for external clouds
- review third-party actions before using them
- keep artifact retention low
- avoid logging secrets
- use non-root containers
- update dependencies regularly

## Team process best practices
- define CODEOWNERS
- use PR templates
- require review before merge
- keep release notes simple and traceable
- keep rollback process documented
