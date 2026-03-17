# DevOps Checklist Mapped to GitHub Actions, Kubernetes, and Terraform

## Purpose

This document is designed for training use. It maps core DevOps principles to three practical implementation layers:

- **GitHub Actions** for CI/CD automation
- **Kubernetes** for application deployment and runtime operations
- **Terraform** for Infrastructure as Code and platform provisioning

Use this as a reference checklist, workshop handout, or foundation for internal engineering standards.

---

# 1. Version Control Everything

## Principle
Everything that defines your system should live in version control.

## Why it matters
Version control gives traceability, rollback capability, peer review, and a single source of truth.

## GitHub Actions
- Store workflow files in `.github/workflows/`
- Version CI/CD logic along with application code
- Enforce pull requests and branch protections before pipelines run on protected branches

## Kubernetes
- Store all manifests in Git:
  - Deployments
  - Services
  - Ingress
  - ConfigMaps
  - Secrets references
  - RBAC definitions
- Prefer GitOps-style delivery where cluster state is derived from Git

## Terraform
- Store:
  - Providers
  - Modules
  - Variables
  - State backend configuration
  - IAM/networking/resource definitions
- Never rely on ad hoc console-created infrastructure without codifying it later

## Training takeaway
If it changes system behavior and is not in Git, it is operational risk.

---

# 2. Trunk-Based Development

## Principle
Keep branches short-lived and merge frequently into the main integration branch.

## Why it matters
This reduces merge conflicts, hidden integration failures, and delayed testing.

## GitHub Actions
- Trigger CI on every push and pull request
- Protect `main` with required checks
- Use feature branches only for short-lived changes
- Use reusable workflows to standardize merge validation

## Kubernetes
- Deploy from the main branch to shared environments
- Use feature flags instead of long-lived environment forks
- Avoid maintaining branch-specific manifests for extended periods

## Terraform
- Keep infrastructure changes small and reviewable
- Run `terraform plan` in pull requests
- Merge incremental infrastructure changes rather than batching massive platform updates

## Training takeaway
Integrate often. Delay creates technical and coordination debt.

---

# 3. Automated CI Pipeline

## Principle
Every change should be validated automatically.

## Why it matters
Fast feedback prevents defective code from propagating and improves engineering throughput.

## GitHub Actions
Typical CI stages:
- Checkout
- Dependency restore/cache
- Lint
- Unit test
- Build
- Package artifact
- Security scanning

Example responsibilities:
- `pytest`, `go test`, `npm test`
- `docker build`
- artifact uploads
- workflow summaries

## Kubernetes
- CI should validate Kubernetes manifests:
  - schema checks
  - linting
  - policy validation
- Build container images intended for deployment into Kubernetes

## Terraform
- CI should run:
  - `terraform fmt -check`
  - `terraform validate`
  - `terraform plan`
- Optionally run cost estimation and policy checks during CI

## Training takeaway
Validation must be machine-driven, repeatable, and visible on every change.

---

# 4. Strong Test Strategy

## Principle
Use a balanced test pyramid: many unit tests, fewer integration tests, and limited E2E tests.

## Why it matters
This gives confidence without making delivery slow or fragile.

## GitHub Actions
- Run different test tiers in separate jobs
- Parallelize where possible
- Publish test results and summaries
- Block merges on critical failures

## Kubernetes
- Run integration and E2E tests against ephemeral or staging clusters
- Validate readiness/liveness behavior
- Test service-to-service connectivity and ingress flows

## Terraform
- Validate infra modules using:
  - `terraform validate`
  - static checks
  - module test environments
- For advanced teams, test module composition in isolated environments

## Training takeaway
Not all tests are equal. Put most validation at the fastest possible layer.

---

# 5. Infrastructure as Code

## Principle
Provision and manage infrastructure through code, not manual clicks.

## Why it matters
IaC improves reproducibility, auditability, consistency, and disaster recovery.

## GitHub Actions
- Automate plan/apply workflows
- Require approval for production applies
- Separate CI validation from deployment permissions
- Store pipeline logic for infrastructure delivery in Git

## Kubernetes
- Cluster add-ons and supporting resources should be declared:
  - namespaces
  - RBAC
  - storage classes
  - ingress controllers
  - autoscalers
- Use declarative manifests or Helm, but keep them versioned

## Terraform
Terraform is the primary implementation mechanism here:
- VPC/network
- Kubernetes cluster
- node pools
- IAM roles
- DNS
- load balancers
- databases
- buckets
- secrets manager resources

## Training takeaway
Manual infrastructure work does not scale and cannot be trusted under pressure.

---

# 6. Immutable Artifacts

## Principle
Build once, then promote the exact same artifact across environments.

## Why it matters
This removes drift between test, staging, and production.

## GitHub Actions
- Build container image once
- Tag with commit SHA, release tag, or both
- Push to a registry such as GHCR
- Promote existing image instead of rebuilding for each environment

## Kubernetes
- Deploy by immutable image reference
- Prefer exact image tags or digests
- Avoid mutable tags like `latest` in production

## Terraform
- Reference immutable artifact identifiers in infrastructure pipelines when needed
- Use versioned module releases and pinned provider versions

## Training takeaway
Rebuilding during promotion undermines reproducibility.

---

# 7. Configuration Management

## Principle
Separate configuration from application code.

## Why it matters
The same application artifact should run in multiple environments with different config.

## GitHub Actions
- Inject configuration through secrets, variables, and environment settings
- Use environment-specific deployment jobs
- Avoid hardcoding endpoints and credentials in workflows

## Kubernetes
- Store non-secret configuration in ConfigMaps
- Inject config through env vars, mounted files, or Helm values
- Keep environment overlays controlled and minimal

## Terraform
- Use variables, tfvars, workspaces, or separate environment folders
- Keep environment differences explicit and reviewable
- Use remote data and outputs carefully to avoid hidden coupling

## Training takeaway
Code should be portable. Configuration should express environment differences cleanly.

---

# 8. Secrets Management

## Principle
Secrets must never be hardcoded in source repositories.

## Why it matters
Hardcoded credentials are a common source of compromise and compliance failure.

## GitHub Actions
- Store secrets in GitHub Secrets or environment secrets
- Restrict production secrets to protected environments
- Use OIDC federation where possible instead of long-lived cloud credentials

## Kubernetes
- Use Secrets for runtime injection
- Prefer external secret managers for production-grade environments
- Limit secret access with RBAC and namespace boundaries

## Terraform
- Provision secret stores and access policies
- Avoid outputting secrets in plaintext
- Mark sensitive variables/outputs appropriately
- Prefer runtime retrieval rather than embedding values into configs

## Training takeaway
The best secret is short-lived, centrally managed, and never committed.

---

# 9. Continuous Deployment / Continuous Delivery

## Principle
Automate the path from validated code to deployable or deployed software.

## Why it matters
Automation reduces human error, improves speed, and makes releases predictable.

## GitHub Actions
- Use multi-stage workflows:
  - CI
  - image publish
  - deploy to dev
  - promote to staging/prod
- Use environment approvals for controlled production release

## Kubernetes
- CD should update deployments, rollout workloads, and observe health
- Use rollout status checks
- Keep release mechanics declarative

## Terraform
- Use Terraform to provision the delivery platform and environment dependencies
- For infrastructure rollout itself, use approved apply workflows

## Training takeaway
Delivery should be a system, not a manual ceremony.

---

# 10. Progressive Delivery

## Principle
Release changes gradually to reduce risk.

## Why it matters
Smaller blast radius means safer releases and faster learning.

## GitHub Actions
- Trigger staged deployment jobs
- Use workflow inputs or environment gates for canary progression
- Integrate release metadata and deployment summaries

## Kubernetes
- Implement:
  - rolling updates
  - canary deployments
  - blue/green deployments
  - feature-flag-aware rollouts
- Use readiness probes and automated rollback signals where available

## Terraform
- Provision the infrastructure required for progressive delivery:
  - load balancers
  - multiple target groups
  - traffic-routing dependencies
  - DNS resources
- Support multiple environments and isolated release lanes

## Training takeaway
Do not expose all users to all risk at once.

---

# 11. Observability

## Principle
Collect enough telemetry to understand system behavior and failures.

## Why it matters
Without observability, teams debug blindly and recover slowly.

## GitHub Actions
- Publish workflow logs, artifacts, test reports, and summaries
- Capture build duration and failure signals
- Notify on pipeline failures

## Kubernetes
Implement the three pillars:
- logs
- metrics
- traces

Common runtime concerns:
- pod restarts
- CPU/memory pressure
- request latency
- error rates
- deployment health
- cluster events

## Terraform
- Provision observability stack resources:
  - monitoring workspaces
  - log sinks
  - dashboards
  - alert channels
  - service accounts
- Keep observability infrastructure reproducible

## Training takeaway
You cannot operate what you cannot see.

---

# 12. SLOs and Alerting

## Principle
Define acceptable reliability targets and alert only on actionable issues.

## Why it matters
Bad alerting creates fatigue. Good alerting protects user experience.

## GitHub Actions
- Alert on failed delivery workflows and broken deployment pipelines
- Use status checks as gate signals
- Route failures to team channels with enough context

## Kubernetes
- Alert on symptoms tied to service health:
  - high latency
  - elevated error rate
  - saturation
  - crash loops
  - failed rollouts
- Base alerts on service objectives, not just raw infrastructure noise

## Terraform
- Provision alert policies and notification channels
- Manage threshold configuration and escalation routing as code

## Training takeaway
Alert on what matters to users and operators, not on every noisy metric.

---

# 13. Shift-Left Security

## Principle
Security checks should happen early and continuously in the delivery lifecycle.

## Why it matters
Late security discovery is expensive and disruptive.

## GitHub Actions
Integrate:
- SAST
- dependency scanning
- secret scanning
- container scanning
- SBOM generation
- license/compliance checks

## Kubernetes
- Validate manifests against security policies
- Enforce least privilege
- Scan images before deployment
- Restrict privileged containers and dangerous capabilities

## Terraform
- Scan Terraform code for risky patterns
- Validate network exposure, IAM over-permissioning, encryption settings, and public access misconfigurations

## Training takeaway
Security should be built into the path to production, not bolted on afterward.

---

# 14. Policy as Code

## Principle
Governance and compliance rules should be enforced automatically.

## Why it matters
Manual enforcement is inconsistent and difficult to scale.

## GitHub Actions
- Run policy checks in PR workflows
- Block merges if required controls fail
- Standardize reusable compliance workflows

## Kubernetes
Examples of policy enforcement:
- disallow privileged containers
- require resource limits
- require labels/annotations
- restrict image registries
- enforce namespace boundaries

## Terraform
- Enforce policy on:
  - tags
  - encryption
  - approved regions
  - instance types
  - public exposure
  - naming standards
- Run policy gates before apply

## Training takeaway
Every important rule should be testable by automation.

---

# 15. Standardization and Golden Paths

## Principle
Provide paved roads that make the right way the easy way.

## Why it matters
Standardization reduces cognitive load, defects, and onboarding time.

## GitHub Actions
- Reusable workflows
- starter pipeline templates
- standard action versions
- common release patterns
- organization-wide workflow conventions

## Kubernetes
- Standard base manifests or Helm charts
- Consistent labels, probes, resources, ingress patterns, and security defaults
- Shared deployment templates for teams

## Terraform
- Standardized modules for:
  - VPC
  - cluster
  - database
  - IAM
  - DNS
  - monitoring
- Versioned module catalog for common platform needs

## Training takeaway
Teams move faster when common engineering problems are already solved well.

---

# 16. Environment Parity

## Principle
Keep development, staging, and production behavior as close as practical.

## Why it matters
Environment drift causes unreliable testing and surprise production failures.

## GitHub Actions
- Use the same build logic for every environment
- Reuse workflows across branches and promotions
- Run tests in containerized, repeatable contexts

## Kubernetes
- Keep staging topology similar to production
- Use the same deployment method and health checks
- Avoid one-off manual patches in any environment

## Terraform
- Provision environments using the same modules with controlled variable differences
- Avoid hand-built staging or production infrastructure

## Training takeaway
The more environments differ, the less trustworthy your validation becomes.

---

# 17. Rollback and Recovery Strategy

## Principle
Every deployment should have a recovery path.

## Why it matters
Incidents are inevitable. Recovery speed matters as much as prevention.

## GitHub Actions
- Keep previous release references available
- Provide manual or automated rollback workflows
- Store deployment metadata and artifact history

## Kubernetes
- Use rollout history where applicable
- Support deployment rollback
- Ensure health probes can detect bad releases quickly
- Keep recovery procedures documented and tested

## Terraform
- Be cautious: infrastructure rollback is not always symmetrical
- Use plans, approvals, backups, versioned modules, and drift awareness
- For stateful resources, recovery often means restore or failover, not simple rollback

## Training takeaway
A release process without rollback is incomplete.

---

# 18. Measure Delivery Performance

## Principle
Track the effectiveness of your delivery system.

## Why it matters
You cannot improve DevOps maturity without measurement.

## GitHub Actions
Measure:
- workflow duration
- build success rate
- deployment frequency
- failed deployment count
- lead time from commit to deploy

## Kubernetes
Measure:
- rollout duration
- failed rollout rate
- pod recovery time
- service availability after deployment

## Terraform
Measure:
- plan/apply duration
- infra change failure rate
- drift incidents
- recovery time for infra problems

## Training takeaway
Use delivery metrics to improve process quality, not to punish teams.

---

# 19. Blameless Postmortems

## Principle
Investigate failures to improve systems, not to assign personal blame.

## Why it matters
Blame suppresses reporting and learning. Systems thinking improves resilience.

## GitHub Actions
- Retain logs and workflow run history
- Capture the exact failing job, commit, and deployment metadata
- Link incident reviews back to pipeline events

## Kubernetes
- Use events, rollout history, pod logs, metrics, and traces in incident analysis
- Document operational contributing factors, not just immediate symptoms

## Terraform
- Review infrastructure plans, applies, state changes, and change history
- Identify gaps in module design, approvals, validation, and policy controls

## Training takeaway
Every incident should leave the system stronger than before.

---

# 20. Documentation and Runbooks

## Principle
Critical operational knowledge must be documented and maintained.

## Why it matters
Good documentation reduces dependency on tribal knowledge and improves response speed.

## GitHub Actions
Document:
- pipeline stages
- required secrets
- approvals
- release triggers
- rollback commands
- troubleshooting steps

## Kubernetes
Document:
- deployment flow
- scaling behavior
- common failure modes
- emergency actions
- service ownership
- on-call procedures

## Terraform
Document:
- module purpose
- variables and outputs
- backend/state model
- apply process
- import strategy
- disaster recovery considerations

## Training takeaway
If an operator needs it during an incident, it should already be written down.

---

# 21. Identity, Access, and Least Privilege

## Principle
Give systems and people only the access they need.

## Why it matters
Excess access expands blast radius and increases security risk.

## GitHub Actions
- Use environment protections
- Limit who can approve production workflows
- Prefer OIDC-based short-lived cloud auth instead of static credentials
- Restrict token permissions in workflows

## Kubernetes
- Use RBAC properly
- Avoid cluster-admin except where absolutely necessary
- Separate service accounts by workload
- Restrict namespace access

## Terraform
- Create least-privilege IAM roles and policies
- Separate plan/apply permissions where appropriate
- Isolate state access carefully

## Training takeaway
Access should be deliberate, minimal, and auditable.

---

# 22. Resource Management and Cost Awareness

## Principle
Reliability and cost efficiency should be engineered together.

## Why it matters
Poor sizing and waste hurt both performance and business efficiency.

## GitHub Actions
- Optimize caching and workflow execution time
- Avoid unnecessary parallel jobs
- Limit expensive CI steps to relevant paths or branches

## Kubernetes
- Define CPU and memory requests/limits appropriately
- Use autoscaling where justified
- Monitor overprovisioning, noisy neighbors, and idle workloads

## Terraform
- Standardize instance sizes and storage classes
- Use tagging for ownership and cost allocation
- Review planned changes for cost impact

## Training takeaway
Good DevOps is not only fast and safe; it is economically responsible.

---

# 23. Drift Detection

## Principle
Detect when real infrastructure or cluster state diverges from declared state.

## Why it matters
Drift makes deployments unpredictable and audits difficult.

## GitHub Actions
- Schedule validation workflows
- Run plan/diff jobs regularly
- Publish drift reports to engineering teams

## Kubernetes
- Compare live state against Git-managed desired state
- Detect manual changes to workloads, policies, or config

## Terraform
- Run periodic `terraform plan` in read-only mode for drift detection
- Investigate unmanaged or manually modified resources promptly

## Training takeaway
Uncontrolled drift silently degrades platform integrity.

---

# 24. Reproducible Environments

## Principle
A new engineer or pipeline should be able to recreate the system consistently.

## Why it matters
Reproducibility improves onboarding, debugging, testing, and disaster recovery.

## GitHub Actions
- Use pinned action versions where appropriate
- Define exact build commands in workflows
- Avoid undocumented local-only assumptions

## Kubernetes
- Use declarative manifests and containerized workloads
- Keep cluster bootstrap and add-on installation documented and codified

## Terraform
- Use remote state, pinned providers, versioned modules, and explicit variable definitions
- Keep bootstrap steps minimal and documented

## Training takeaway
If the environment cannot be recreated reliably, it is fragile.

---

# 25. Separation of Concerns Across the Stack

## Principle
Keep application delivery, runtime operations, and infrastructure provisioning logically distinct but well integrated.

## Why it matters
Clear boundaries improve ownership, safety, and maintainability.

## GitHub Actions
- Use separate workflows for:
  - CI validation
  - image publishing
  - application deployment
  - infrastructure deployment
- Keep permission scopes appropriate to each workflow

## Kubernetes
- Focus on runtime concerns:
  - scheduling
  - networking
  - scaling
  - rollout
  - service exposure
- Do not overload Kubernetes manifests with unrelated infra concerns

## Terraform
- Focus on provisioning:
  - cloud foundation
  - networking
  - IAM
  - cluster creation
  - managed services
- Avoid mixing every operational concern into Terraform unnecessarily

## Training takeaway
Integration is important, but separation of responsibilities prevents chaos.

---

# Suggested Training Exercise

Use this checklist to design a sample delivery platform for one application:

1. **Terraform**
   - Provision VPC, Kubernetes cluster, IAM, container registry access, DNS, and monitoring prerequisites

2. **GitHub Actions**
   - Build and test the application
   - Build container image
   - Push image to registry
   - Run Terraform validation
   - Deploy application to Kubernetes
   - Publish workflow summary

3. **Kubernetes**
   - Deploy application with:
     - Deployment
     - Service
     - Ingress
     - ConfigMap
     - Secret reference
     - resource limits
     - probes

4. **Operational add-ons**
   - Monitoring
   - Alerting
   - rollout checks
   - rollback workflow
   - policy enforcement

---

# Final Summary

A solid DevOps implementation is not just a set of tools. It is an operating model where:

- **GitHub Actions** automates validation and delivery
- **Kubernetes** runs and operates workloads consistently
- **Terraform** provisions and governs infrastructure predictably

The best teams make all three work together through:
- version control
- automation
- observability
- security
- standardization
- recovery planning
- continuous improvement

---

# Quick Reference Matrix

| Principle | GitHub Actions | Kubernetes | Terraform |
|---|---|---|---|
| Version control | Workflows in Git | Manifests in Git | IaC in Git |
| CI automation | Build/test/scan on every change | Validate deployable manifests | fmt/validate/plan |
| CD | Deploy workflows and approvals | Rollouts and health checks | Infra apply workflow |
| Immutable delivery | Build once and tag images | Deploy exact image tag/digest | Pin versions and modules |
| Config | Variables and environments | ConfigMaps and values | Variables and environment definitions |
| Secrets | GitHub Secrets / OIDC | Secrets / external secret store | Secret manager resources and IAM |
| Security | SAST, scans, policy checks | RBAC, secure manifests, image controls | IaC scanning and IAM controls |
| Observability | Pipeline logs and summaries | Logs, metrics, traces | Monitoring resources as code |
| Rollback | Workflow-driven redeploys | Rollout undo / redeploy | Controlled recovery and restore |
| Standardization | Reusable workflows | Base charts/manifests | Reusable modules |

