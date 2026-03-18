# Appian DevOps Extended Guide (CI/CD, YAML, Diagrams)

---

## 1. Overview

Appian is a **closed-source PaaS platform**.

- No VM access
- No custom runner installation
- Deployment via APIs

👉 DevOps is **API-driven**

---

## 2. CI/CD Architecture Diagram

```
Developer
   ↓
Appian Dev Environment
   ↓
GitHub Actions (CI)
   ├── Export Package
   ├── Inspect Package
   ├── Store Artifact
   ↓
GitHub Actions (CD)
   ├── Inspect (Target)
   ├── Deploy via API
   ├── Fetch Logs
   ↓
Appian QA / PROD
```

---

## 3. Appian CI Pipeline (GitHub Actions)

```yaml
name: Appian CI

on:
  push:
    branches: [ main ]

jobs:
  ci:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Export Package
        run: |
          curl -X POST           "${{ secrets.APPIAN_URL }}/suite/deployment-management/v2/deployments"           -H "appian-api-key: ${{ secrets.APPIAN_API_KEY }}"           -H "Action-Type: export"           -o export.json

      - name: Inspect Package
        run: |
          curl -X POST           "${{ secrets.APPIAN_URL }}/suite/deployment-management/v2/inspections"           -H "appian-api-key: ${{ secrets.APPIAN_API_KEY }}"           -F "packageFile=@appian-package.zip"
```

---

## 4. Appian CD Pipeline (GitHub Actions)

```yaml
name: Appian CD

on:
  push:
    tags:
      - "v*"

jobs:
  cd:
    runs-on: ubuntu-latest

    steps:
      - name: Deploy Package
        run: |
          curl -X POST           "${{ secrets.APPIAN_URL }}/suite/deployment-management/v2/deployments"           -H "appian-api-key: ${{ secrets.APPIAN_API_KEY }}"           -H "Action-Type: import"           -F "packageFile=@appian-package.zip"           -o deploy.json

      - name: Get Logs
        run: |
          UUID=$(cat deploy.json | jq -r '.uuid')

          curl           "${{ secrets.APPIAN_URL }}/suite/deployment-management/v2/deployments/$UUID/log"           -H "appian-api-key: ${{ secrets.APPIAN_API_KEY }}"
```

---

## 5. Deployment Flow Diagram

```
CI Phase:
---------
Code → Export → Inspect → Artifact

CD Phase:
---------
Artifact → Inspect(Target) → Deploy → Verify Logs
```

---

## 6. Best Practices

- Always inspect before deploy
- Use versioned tags (v1.0.0)
- Use GitHub Secrets for API keys
- Promote across environments (Dev → QA → Prod)
- Never manually modify higher env

---

## 7. Limitations

- No infrastructure control
- No Docker/Kubernetes
- No custom scripts inside Appian
- Limited automation scope

---

## 8. Comparison

| Feature | Kubernetes | Appian |
|--------|-----------|--------|
| CI/CD | Full | API-based |
| Infra control | Yes | No |
| Deployment | Image | Package |

---

## 9. Key Takeaway

```
Appian DevOps = API-driven promotion model
```

---

End of Document
