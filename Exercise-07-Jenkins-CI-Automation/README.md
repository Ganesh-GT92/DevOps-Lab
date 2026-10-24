# Exercise 07: Jenkins CI Automation & Setup

## Objective
Understand Continuous Integration (CI) concepts, explore modern CI/CD tooling, install and configure Jenkins using Docker, retrieve administrative credentials, and initialize the Jenkins automation server for automated build and test pipelines.

---

## 1. What is Continuous Integration (CI)?
Continuous Integration (CI) is a software development practice where developers frequently commit and merge code changes into a central repository. Automated builds and automated tests are triggered immediately upon each commit to detect and resolve defects early, accelerating delivery and safeguarding code stability.

### Key Pillars of CI
1. **Frequent Integration**: Developers commit changes multiple times per day.
2. **Automated Builds**: Automated systems compile, package, and containerize code upon integration.
3. **Automated Testing**: Test suites (unit, integration, linting) validate code functionality and prevent regressions.
4. **Immediate Feedback**: Developers receive real-time build and test status reports.

### Key Benefits
- **Early Bug Detection**: Bugs are isolated to small, recent commits.
- **Improved Collaboration**: Minimizes merge conflicts and integration hell.
- **Fast Development Cycles**: Reduces manual QA and deployment overhead.
- **High Software Quality**: Enforces automated quality gates before release.

---

## 2. CI/CD Tools Overview

| Tool | Deployment Model | Key Highlights | Best Used For |
|---|---|---|---|
| **Jenkins** | Self-hosted / Containerized | Open-source, 1800+ plugins, extreme extensibility | Universal enterprise CI/CD & custom pipelines |
| **GitHub Actions** | Cloud / Self-hosted Runners | Native GitHub integration, YAML workflows, vast marketplace | Teams using GitHub version control |
| **GitLab CI/CD** | Cloud / Self-hosted | Built into GitLab, Auto-DevOps, native container registries | Teams hosting on GitLab |
| **CircleCI** | Cloud / Containerized | High parallelism, advanced caching, rapid build times | Modern microservice architectures |
| **Azure DevOps** | Cloud / Hybrid | Deep Azure/Visual Studio integration, enterprise governance | Enterprise Windows & Azure environments |

---

## 3. Jenkins Architecture & Installation

### Docker Setup
Jenkins is deployed as an isolated Docker container exposing port `8080` (HTTP Web UI) and port `50000` (build agent communication protocol), with persistent volume storage for `/var/jenkins_home`.

```powershell
docker run -d --name jenkins `
  -p 8080:8080 -p 50000:50000 `
  -v jenkins_home:/var/jenkins_home `
  jenkins/jenkins:lts
```

### Retrieving Initial Administrator Password
On the initial run, Jenkins generates a secure setup key stored inside the container volume:
```powershell
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

---

## 4. Verification Evidence & Screenshots

| Step | Screenshot | Description |
|---|---|---|
| **Unlock Jenkins** | `screenshots/01-jenkins-unlock.png` | Initial unlock screen prompting for administrator password |
| **Plugin Installation** | `screenshots/02-jenkins-plugins.png` | "Customize Jenkins" / "Install suggested plugins" setup screen |
| **Jenkins Ready Dashboard** | `screenshots/03-jenkins-ready.png` | Jenkins main dashboard / "Welcome to Jenkins" landing page |

---

## 5. Summary & Next Steps
Jenkins has been successfully containerized, initialized, and verified on port `8080`. The environment is primed to execute automated freestyle and multi-stage pipeline jobs in the subsequent exercises.
