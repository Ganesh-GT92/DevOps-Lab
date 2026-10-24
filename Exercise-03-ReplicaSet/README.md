

\# Exercise 3: Scaling Flask App Using ReplicaSets



\## Objective

Understand ReplicaSets and Pods, scale a Flask application, and observe automatic Pod recovery using Minikube.



\## Application Endpoints

\- `/` — Welcomes users to the Big Sale and identifies the serving Pod.

\- `/buy?user=123` — Simulates a purchase and reports which Pod handled it.

\- `/health` — Returns the application's health status.



\## Implementation

1\. Built the `flashsale:1.0` Docker image inside Minikube.

2\. Created a ReplicaSet with 3 replicas.

3\. Scaled the ReplicaSet to 5 replicas.

4\. Deleted one Pod and verified that Kubernetes created a replacement.

5\. Tested all three Flask endpoints using port forwarding.



\## Results

\- Initial replicas: 3

\- Scaled replicas: 5

\- Replicas after Pod replacement: 5

\- Homepage, buy, and health endpoints: successful



\## Technologies

Python, Flask, Gunicorn, Docker, Kubernetes, Minikube, kubectl, YAML.



\## Evidence

Screenshots are stored in the `screenshots/` folder.



