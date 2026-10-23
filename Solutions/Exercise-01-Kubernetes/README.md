\# Exercise 1: Kubernetes — Hello Pod



\## Objective

Deploy an Nginx web server on a local Kubernetes cluster using Minikube, expose it through a NodePort Service, and access it in a browser.



\## Environment

\- Operating System: Windows 11

\- Container Runtime: Docker Desktop

\- Kubernetes Cluster: Minikube

\- Container Image: nginx

\- Application Port: 80



\## Implementation Steps



\### 1. Start the Kubernetes cluster

```powershell

minikube start --driver=docker

```



\### 2. Verify the cluster

```powershell

kubectl get nodes

```

Result: The Minikube node reached the Ready status.



\### 3. Create the Pod

```powershell

kubectl run hello-k8s --image=nginx --port=80

```



\### 4. Verify the Pod

```powershell

kubectl get pods

```

Result: The hello-k8s Pod reached the Running status with 1/1 containers ready.



\### 5. Expose the Pod

```powershell

kubectl expose pod hello-k8s --type=NodePort --port=80

```



\### 6. Verify the Service

```powershell

kubectl get services

kubectl describe service hello-k8s

```

Result: The hello-k8s Service was created with NodePort type and exposed container port 80.



\### 7. Access the application

```powershell

minikube service hello-k8s

```

Result: The Nginx welcome page opened successfully in the browser.



\## Evidence

\- `01-minikube-ready.png` — Kubernetes node status

\- `02-hello-pod-running.png` — Pod running status

\- `03-hello-service.png` — Service details

\- `04-nginx-browser.png` — Nginx welcome page

\- `05-service-details.png` — Service description and access URL



\## Conclusion

Successfully deployed an Nginx container as a Kubernetes Pod, exposed it using a NodePort Service, and verified browser access through Minikube.



