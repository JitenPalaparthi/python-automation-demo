# Git Flow for Participants

## 1. Goal
This is a simple, practical Git flow for training participants.
It avoids unnecessary complexity and works well for automation projects.

## 2. Main idea
Use:
- `main` for stable, production-ready code
- `feature/*` for new work
- `bugfix/*` for fixes
- `hotfix/*` for urgent production fixes

## 3. Day-to-day workflow
1. Pull the latest code from `main`
2. Create a short-lived branch
3. Make changes in small logical steps
4. Commit with clear messages
5. Push the branch
6. Raise a Pull Request
7. Merge only after review and CI success

## 4. Example flow
```bash
git checkout main
git pull origin main
git checkout -b feature/add-checkout-test
# make changes
git add tests/test_cart_checkout.py
git commit -m "test: add checkout coverage"
git push -u origin feature/add-checkout-test
```

## 5. Pull Request rules
- no direct push to `main`
- every change goes through PR
- at least one review
- CI must pass
- resolve conflicts before merge

## 6. Release flow
```bash
git checkout main
git pull origin main
git tag v1.0.0
git push origin main --tags
```

That release tag triggers the GHCR publish workflow.

## 7. Branch naming examples
- `feature/login-page`
- `feature/add-api-tests`
- `bugfix/cart-counter`
- `hotfix/security-header`
- `release/v1.2.0`

## 8. Commit message examples
- `feat: add login page object`
- `test: add network mocking scenario`
- `fix: correct checkout assertion`
- `chore: update CI workflow`
- `docs: add GHCR release notes`

## 9. What participants should remember
- branch from `main`
- keep branches short-lived
- commit often, but with meaning
- do not commit secrets
- do not merge broken code
- release with tags, not random manual deployment
