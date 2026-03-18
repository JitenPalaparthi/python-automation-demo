# DevOps + Appian CI/CD Training Repository

## 📌 Overview

This repository demonstrates:

- CI pipeline using GitHub Actions (`ci.yaml`)
- CD pipeline using GitHub Actions (`cd.yaml`)
- Hands-on DevOps practices (Kubernetes, Docker, GHCR)
- Appian CI/CD using Deployment APIs
- Supporting documentation for learning and training

---

## ⚙️ CI Pipeline (`ci.yaml`)

The CI pipeline is triggered on:

- Every code push
- Pull requests
- Manual trigger

### What it does:

- Installs dependencies
- Runs Playwright-based Python tests
- Generates test reports
- Publishes test summary in GitHub UI
- Runs security scanning (CodeQL)

👉 Purpose:
- Validate code quality
- Ensure application correctness
- Catch issues early (shift-left)

---

## 🚀 CD Pipeline (`cd.yaml`)

The CD pipeline is triggered on:

- Git tags (e.g., `v1.0.0`)
- Manual trigger

### What it does:

- Builds Docker image (multi-arch)
- Pushes image to GHCR
- Deploys to Kubernetes cluster (via self-hosted runner)
- Updates deployment and verifies rollout

👉 Purpose:
- Release automation
- Controlled deployment using version tags
- Infrastructure-based deployment (Kubernetes)

---

## 🧠 Appian CI/CD Concept

Unlike Kubernetes-based systems, Appian works differently.

### Key Points:

- Appian is a **closed-source PaaS**
- No access to infrastructure (VMs)
- No GitHub runners inside Appian

👉 So:

- CI → possible (validation, export, inspection)
- CD → limited (API-based deployment only)

---

## 📄 Documentation Included

### 1. `appian-devops-guide.md`

Covers:

- Appian DevOps fundamentals
- CI/CD concepts in Appian
- Best practices
- Limitations
- Comparison with Kubernetes

---

### 2. `appian-devops-extended.md`

Includes:

- CI/CD YAML examples for Appian
- API-based deployment flows
- Architecture diagrams
- End-to-end pipeline explanation

---

## 🔄 DevOps Flow (Summary)

### Standard Application (Kubernetes)

```
Code → CI → Build → GHCR → CD → Kubernetes
```

### Appian

```
Appian Dev → Export → Inspect → Package → Deploy via API
```

---

## ⚠️ Key Differences

| Feature | Kubernetes | Appian |
|--------|-----------|--------|
| Infra access | Yes | No |
| CI/CD | Full | Limited |
| Deployment | Container-based | Package-based |
| Automation | Full | API-driven |

---

## 🎯 Key Takeaways

- CI/CD works fully in open/cloud-native systems
- Appian uses a **controlled deployment model**
- DevOps in Appian is **API-driven, not infrastructure-driven**

---

## 👨‍💻 Author / Trainer

JP  
DevOps | Cloud | Golang | Rust | Architecture

---

## 📢 Note

This repository is designed for **training and learning purposes** to understand:

- Real-world DevOps pipelines
- Differences between open systems and PaaS platforms like Appian

---
