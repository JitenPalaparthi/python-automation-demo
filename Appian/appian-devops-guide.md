# Appian DevOps Guide (CI/CD, Best Practices, Limitations)

## 1. Overview

Appian is a **closed-source PaaS (Platform as a Service)** platform.

- No access to underlying VMs
- No ability to install custom agents/runners
- Deployment is controlled via Appian-provided mechanisms

👉 DevOps with Appian is **API-driven**, not infrastructure-driven.

---

## 2. CI/CD in Appian

### CI (Continuous Integration)

- Validate application changes
- Export applications/packages
- Inspect packages for issues
- Store artifacts (ZIP files)

### CD (Continuous Deployment)

- Import packages into target environments
- Use Appian Deployment APIs
- Validate deployment logs

---

## 3. Architecture

```
Developer → Appian Dev Env
        ↓
GitHub Actions (CI)
        ↓
Export + Inspect
        ↓
Artifacts (ZIP)
        ↓
CD Pipeline
        ↓
Appian QA/Prod (Import via API)
```

---

## 4. Key APIs

Base URL:
```
/suite/deployment-management/v2
```

### Inspect Package
```
POST /inspections
```

### Deploy (Import)
```
POST /deployments
Header: Action-Type: import
```

### Export
```
POST /deployments
Header: Action-Type: export
```

### Deployment Logs
```
GET /deployments/{uuid}/log
```

---

## 5. Authentication

- API Key (Service Account)
- OAuth 2.0 (optional)

Header example:
```
appian-api-key: <KEY>
```

---

## 6. Best Practices

### Pipeline

- Always run **inspection before deployment**
- Fail pipeline on critical errors
- Store artifacts for traceability

### Versioning

- Use versioned packages
- Avoid manual changes in higher environments

### Environment Strategy

- Dev → QA → Prod
- Use promotion, not direct changes

### Security

- Store API keys in GitHub Secrets
- Do not hardcode credentials

### Observability

- Always fetch deployment logs
- Track failures and retries

---

## 7. Limitations

### Infrastructure

- No VM access
- Cannot install GitHub runners
- Cannot run arbitrary scripts inside Appian

### Deployment

- No true "continuous deployment"
- Controlled import process
- Limited automation flexibility

### Testing

- No native unit testing framework like code-based apps
- Testing is mostly UI/process-driven

### Customization

- Limited low-level control
- Dependent on platform capabilities

---

## 8. Comparison with Kubernetes

| Feature | Kubernetes | Appian |
|--------|-----------|--------|
| Infra control | Full | None |
| CI/CD | Full | Limited/API-based |
| Custom runners | Yes | No |
| Deployment | Code-driven | Package-driven |

---

## 9. Common Pitfalls

- Trying to treat Appian like a microservice platform
- Skipping inspection step
- Hardcoding credentials
- Not versioning packages

---

## 10. Recommended Tools

- GitHub Actions (or Jenkins)
- Artifact storage (S3 / GitHub artifacts)
- Monitoring via Appian logs

---

## 11. Further Reading

- https://docs.appian.com/suite/help/latest/Deployment_Rest_API.html
- https://docs.appian.com/suite/help/latest/Deploy_to_Target_Environments.html
- https://docs.appian.com/suite/help/latest/Application_Deployment_Guidelines.html
- https://docs.github.com/actions

---

## 12. Key Takeaway

```
Appian DevOps = API-driven deployment, not infrastructure-driven automation
```

- CI is achievable
- CD is controlled and limited
- Platform constraints define architecture

---

## 13. Summary

- Appian supports DevOps via APIs
- No direct infrastructure access
- Focus on package-based promotion
- External tools orchestrate CI/CD

---

End of Document
