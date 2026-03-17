# CI/CD Guidelines for Training Participants

## CI means
Continuous Integration means every change is validated automatically.

Typical CI steps in this project:
1. checkout code
2. setup Python
3. install dependencies
4. install Playwright browser
5. run lint
6. run tests
7. upload reports

## CD means
Continuous Delivery / Deployment means validated code is packaged and published automatically.

In this project, CD publishes a Docker image to GHCR when a version tag is pushed.

## Why CI matters
- catches mistakes early
- keeps `main` stable
- gives confidence before merge
- creates a standard engineering process

## Why CD matters
- makes releases repeatable
- removes manual deployment mistakes
- provides versioned artifacts
- makes rollback easier

## Good CI/CD rules
- do not skip CI
- do not merge red builds
- release from tags
- keep workflow permissions minimal
- keep pipelines understandable
- keep environment-specific secrets outside the repo

## Example release sequence
```bash
git checkout main
git pull origin main
git tag v1.0.0
git push origin main --tags
```

Result:
- GitHub Actions CD workflow starts
- Docker image is built
- image is pushed to GHCR
- image becomes available for pull and deployment
