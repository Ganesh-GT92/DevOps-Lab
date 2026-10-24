# Exercise 10: Minikube Multi-Node Multi-App Deployment

## Objective
Design, build, deploy, and verify a resilient multi-node Kubernetes architecture on Minikube (`devops-multinode` profile with 3 nodes). The deployment hosts two microservices—**Product Catalog** (2 replicas) and **Shopping Cart** (3 replicas)—distributed across independent worker nodes using Kubernetes `podAntiAffinity` rules to achieve high availability and fault tolerance.

---

## Architecture & Topology

```text
                  [ Minikube Cluster: devops-multinode ]
  -------------------------------------------------------------------------
  | Node 1: devops-multinode  | Node 2: devops-multinode-m02 | Node 3: devops-multinode-m03 |
  | (Control Plane / Worker)  | (Worker Node)                | (Worker Node)                |
  |---------------------------|------------------------------|------------------------------|
  | [Shopping Cart Pod #1]    | [Shopping Cart Pod #2]       | [Shopping Cart Pod #3]       |
  |                           | [Product Catalog Pod #1]     | [Product Catalog Pod #2]     |
  -------------------------------------------------------------------------
```

- **Pod Anti-Affinity Enforcement**:
  Each service specifies `topologyKey: "kubernetes.io/hostname"`, forcing the Kubernetes scheduler to place replicas on separate nodes rather than co-locating them on the same physical host.

---

## Directory Structure and Files
```text
Exercise-10-Minikube-Multi-Node-Multi-App/
├── product_catalog.py                  # Product Catalog Flask API (/products)
├── shopping_cart.py                    # Shopping Cart Flask API (/cart GET & POST)
├── Dockerfile.product                  # Container specification for Product Catalog
├── Dockerfile.shopping                 # Container specification for Shopping Cart
├── product_catalog_deployment.yaml     # Kubernetes Deployment (2 replicas + podAntiAffinity)
├── shopping_cart_deployment.yaml        # Kubernetes Deployment (3 replicas + podAntiAffinity)
├── product_catalog_service.yaml        # NodePort service exposing Product Catalog
├── shopping_cart_service.yaml           # NodePort service exposing Shopping Cart
├── README.md                           # Documentation, topology details, and test logs
└── screenshots/                        # Verification screenshots
    ├── 01-minikube-nodes.png           # kubectl get nodes showing all 3 nodes Ready
    ├── 02-pods-distribution.png        # kubectl get pods -o wide showing node distribution
    ├── 03-services.png                 # kubectl get svc showing NodePort services
    └── 04-curl-tests.png               # curl command execution and endpoint responses
```

---

## Execution Steps

### 1. Multi-Node Cluster Initialization
```powershell
minikube start --nodes 3 -p devops-multinode
```

### 2. Containerization
```powershell
docker build -t product-catalog:latest -f Dockerfile.product .
docker build -t shopping-cart:latest -f Dockerfile.shopping .
```

### 3. Load Images into Minikube Nodes
```powershell
minikube -p devops-multinode image load product-catalog:latest
minikube -p devops-multinode image load shopping-cart:latest
```

### 4. Deploy Manifests
```powershell
kubectl apply -f product_catalog_deployment.yaml
kubectl apply -f shopping_cart_deployment.yaml
kubectl apply -f product_catalog_service.yaml
kubectl apply -f shopping_cart_service.yaml
```

---

## Verification Evidence & Screenshots

| Evidence | Screenshot File | Description |
|---|---|---|
| **Multi-Node Cluster** | `screenshots/01-minikube-nodes.png` | Verifies `devops-multinode`, `devops-multinode-m02`, and `devops-multinode-m03` are Ready |
| **Pod Distribution** | `screenshots/02-pods-distribution.png` | Verifies pods are distributed across the 3 nodes via `podAntiAffinity` |
| **Kubernetes Services** | `screenshots/03-services.png` | Displays active NodePort services for both microservices |
| **Endpoint Testing** | `screenshots/04-curl-tests.png` | Verifies `/products` (GET) and `/cart` (GET & POST) endpoints return expected JSON |

---

## Test Verification Summary
- **Nodes**: 3 distinct nodes active and healthy in Minikube.
- **Product Catalog (2 replicas)**: Scheduled across `devops-multinode-m02` and `devops-multinode-m03`.
- **Shopping Cart (3 replicas)**: Distributed evenly across `devops-multinode`, `devops-multinode-m02`, and `devops-multinode-m03`.
- **High Availability**: Successfully validated via anti-affinity topology scheduling.
