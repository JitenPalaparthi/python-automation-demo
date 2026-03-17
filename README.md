# Playwright Python Automation Project with Git, CI/CD and GHCR

This is a moderate, working Playwright automation project in **Python** built for training and explanation.

It is designed to help participants understand:
- Playwright with Python and pytest
- Page Object Model
- UI + API validation
- network mocking
- Git flow and Git best practices
- GitHub Actions CI
- CD up to **GitHub Container Registry (GHCR)**
- security-first DevOps practices

## Project features
- Flask demo app used as the test target
- Playwright Python tests with pytest plugin
- login test flow
- cart and checkout test flow
- API health test
- mocked API response test
- linting with Ruff
- CI workflow for pull requests and main branch pushes
- CD workflow that builds and publishes a Docker image to GHCR on semantic version tags

## Project structure
```text
app/                      Flask demo application
tests/                    UI and API tests
tests/pages/              Page Object Model classes
.github/workflows/        GitHub Actions CI/CD
docs/git-flow.md          Participant-facing Git workflow notes
docs/devops-best-practices.md
docs/ci-cd-guidelines.md
scripts/init-git.sh       Helper to initialize and push to GitHub
Dockerfile                Runtime image for demo deployment
Makefile                  Common local commands
```

## Why this project uses Python Playwright
Playwright supports Python, and the official Python documentation recommends the **pytest plugin** for end-to-end testing. The same docs also describe how to run Playwright in CI by installing browsers and then running `pytest`. citeturn182697search4turn182697search16

## Local setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install --with-deps chromium
python app/app.py
```

Run tests in another terminal:
```bash
source .venv/bin/activate
pytest
```

## Common commands
```bash
make setup
make lint
make test
make run
```

## Git flow for participants
```bash
git checkout main
git pull origin main
git checkout -b feature/add-new-test
# do your changes
git add .
git commit -m "test: add checkout validation"
git push -u origin feature/add-new-test
```

Then raise a Pull Request.
Merge only after review + CI success.

More detailed participant notes are in:
- `docs/git-flow.md`
- `docs/devops-best-practices.md`
- `docs/ci-cd-guidelines.md`

## Initialize Git and push to GitHub
```bash
chmod +x scripts/init-git.sh
./scripts/init-git.sh https://github.com/<your-user>/<your-repo>.git main
```

## CI overview
GitHub Actions workflows live under `.github/workflows`. GitHub’s Actions docs cover workflow automation, and Playwright’s CI docs show the standard flow: install dependencies, install browsers, then run tests. citeturn182697search6turn182697search16

This repo's CI pipeline does the following:
1. checkout code
2. setup Python
3. install dependencies
4. install Playwright Chromium and OS dependencies
5. run Ruff lint
6. run pytest suite
7. upload Playwright artifacts for debugging

## CD to GHCR
This project publishes a Docker image to **GitHub Container Registry** on semantic tags like `v1.0.0`. GitHub’s official docs describe publishing Docker images from Actions and how the container registry works. citeturn182697search1turn182697search5

Release example:
```bash
git checkout main
git pull origin main
git tag v1.0.0
git push origin main --tags
```

Published image pattern:
```text
ghcr.io/<your-org-or-user>/playwright-python-demo:v1.0.0
```

## Recommended repository settings
- protect `main`
- require pull request review
- require CI checks before merge
- restrict who can push tags for releases
- use GitHub Environments for production approvals
- enable Dependabot / dependency review if available

GitHub recommends secure workflow usage, least-privilege permissions, and careful use of third-party actions. citeturn182697search2turn182697search10

## Security notes
- never commit secrets, `.env`, or real credentials
- keep GitHub Actions permissions minimal
- prefer short-lived credentials where possible
- keep artifact retention small because screenshots and traces can expose data
- use a non-root runtime container
- pin and review third-party actions

GitHub’s secure-use reference explicitly recommends minimizing permissions and carefully reviewing actions used in workflows. citeturn182697search2turn182697search22
