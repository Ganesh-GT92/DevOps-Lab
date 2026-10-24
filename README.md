# DevOps Practical Engineering Lab & Projects

A comprehensive hands-on DevOps laboratory repository showcasing end-to-end implementations of containerization, continuous integration, container security, distributed monitoring, and multi-node Kubernetes cluster orchestration.

---

## 🛠️ Technology Stack & Tools

- **Containerization & Runtimes:** Docker, Docker Compose, Containerd
- **Cluster Orchestration:** Kubernetes (Minikube multi-node cluster, kubectl)
- **Continuous Integration / Continuous Delivery (CI/CD):** Jenkins (Declarative multi-stage pipelines)
- **Monitoring & Observability:** Prometheus (Time-series metrics, alert rules), Grafana (Interactive operational dashboards)
- **Application & Testing:** Python 3 (Flask REST APIs, unittest), Bash shell scripting
- **Security & Networking:** AppArmor container security profiles, Docker custom bridge networks

---

## 📂 Repository Structure & Lab Modules

| Directory | Module / Exercise | Focus Area & Description |
|:---|:---|:---|
| [`Exercise-01-Kubernetes`](./Exercise-01-Kubernetes) | **Kubernetes Fundamentals** | Cluster setup, Pod deployment, and service connectivity verification. |
| [`Exercise-02-Minikube-Flask`](./Exercise-02-Minikube-Flask) | **Flask on Kubernetes** | Containerizing a Flask web application, building within Minikube, and exposing via NodePort. |
| [`Exercise-03-ReplicaSet`](./Exercise-03-ReplicaSet) | **Scaling with ReplicaSets** | High-availability flash-sale application with auto-healing and scaling replicas. |
| [`Exercise-04-Docker-Networking`](./Exercise-04-Docker-Networking) | **Docker Custom Networking** | Multi-container microservices architecture (Flask + MySQL + Redis) communicating on a dedicated bridge network. |
| [`Exercise-05-Docker-Security-AppArmor`](./Exercise-05-Docker-Security-AppArmor) | **Container Security (AppArmor)** | Implementing security profiles with Docker SDK for Python to restrict unauthorized OS-level operations. |
| [`Exercise-06-Grafana-Monitoring`](./Exercise-06-Grafana-Monitoring) | **Real-Time Observability** | Live delivery metrics generator, Prometheus scraping, automated alert rules, and 4-panel Grafana monitoring dashboard. |
| [`Exercise-07-Jenkins-CI-Automation`](./Exercise-07-Jenkins-CI-Automation) | **Jenkins CI Initialization** | Containerized Jenkins deployment, admin credentials lifecycle, and baseline plugin configuration. |
| [`Exercise-08-Jenkins-Hello-World`](./Exercise-08-Jenkins-Hello-World) | **Jenkins Freestyle Automation** | Creating and executing a Freestyle build job running custom shell scripts with console verification. |
| [`Exercise-09-Jenkins-Multi-Stage-Pipeline`](./Exercise-09-Jenkins-Multi-Stage-Pipeline) | **Multi-Stage CI/CD Pipeline** | Automated 5-stage declarative pipeline (Build, Unit Test, Staging Deploy, Background Run, and Validation). |
| [`Exercise-10-Minikube-Multi-Node-Multi-App`](./Exercise-10-Minikube-Multi-Node-Multi-App) | **Multi-Node Cluster Deployment** | 3-node Kubernetes cluster hosting independent microservices (Product Catalog & Shopping Cart) distributed via `podAntiAffinity`. |

---

## 🚀 Key Highlights & Architectural Implementations

1. **High Availability & Fault Tolerance**:
   - Implemented Kubernetes `podAntiAffinity` scheduling across a 3-node cluster to guarantee that application replicas reside on separate physical worker nodes.

2. **Automated CI/CD Quality Gates**:
   - Built declarative pipelines in Jenkins that compile, run unit test suites, stage artifacts, and safely manage background processes.

3. **Full-Stack Observability**:
   - Instrumented custom application metrics using `prometheus-client`, configured Prometheus time-series scraping with threshold alerting rules, and visualized operational telemetry in Grafana.

4. **Microservices Communication**:
   - Established isolated container bridge networks for seamless inter-service communication without exposing internal services directly to the public network.

---

## ⚙️ Environment Setup

- **Host OS:** Windows 11 (PowerShell & WSL2)
- **Container Engine:** Docker Desktop (WSL2 engine backend)
- **Local Kubernetes:** Minikube v1.39+ with multi-node profiles (`devops-multinode`)
- **Python Runtime:** Python 3.11+
