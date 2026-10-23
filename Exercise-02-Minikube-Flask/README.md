

\# Exercise 2: Deploy Flask on Minikube



\## Objective

Deploy a Python Flask application on a local Kubernetes cluster using Minikube, Docker, kubectl, and YAML configuration files.



\## Files

\- `app.py` — Flask application.

\- `Dockerfile` — Builds the Flask container image.

\- `flask-deployment.yaml` — Defines the Kubernetes Deployment and NodePort Service.

\- `screenshots/` — Evidence of deployment and successful testing.



\## Implementation Steps

1\. Verified that Minikube was running and the Kubernetes node was Ready.

2\. Created a Flask application listening on port 15000.

3\. Built the `flask-app:latest` image using `minikube image build`.

4\. Created and applied the Kubernetes Deployment.

5\. Verified that the Deployment had one available replica and the Pod was Running.

6\. Created the `flask-app-service` NodePort Service.

7\. Accessed the application using `minikube service flask-app-service --url`.

8\. Tested the application using `curl.exe`.



\## Verification

The application returned:



`Hello from Flask on Kubernetes!`



\## Technologies Used

\- Python

\- Flask

\- Docker

\- Kubernetes

\- Minikube

\- kubectl



