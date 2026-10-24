\# Exercise 4: Docker Networking



\## Objective

Create a user-defined Docker bridge network and run a Flask REST API, MySQL, and Redis containers on the same network.



\## Technologies Used

\- Docker

\- Docker Bridge Networking

\- Python

\- Flask

\- MySQL

\- Redis



\## Implementation Steps



\### 1. Create a Docker Bridge Network

```bash

docker network create --driver bridge my-bridge-net

docker network ls

docker network inspect my-bridge-net

```



\### 2. Build the Flask API Image

```bash

docker build --no-cache --build-arg PIP\_DEFAULT\_TIMEOUT=120 -t flask-api .

```



\### 3. Start the MySQL Container

```bash

docker run -d --name mysql --network my-bridge-net -e "MYSQL\_ROOT\_PASSWORD=DevLab123!" mysql:latest

```



\### 4. Start the Redis Container

```bash

docker run -d --name redis --network my-bridge-net redis:latest

```



\### 5. Start the Flask Container

```bash

docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api

```



\### 6. Verify Containers and Network Connectivity

```bash

docker ps

docker network inspect my-bridge-net

docker exec flask python -c "import socket; print('MySQL IP:', socket.gethostbyname('mysql')); print('Redis IP:', socket.gethostbyname('redis'))"

```



\### 7. Test the API

```bash

curl.exe http://localhost:5001/about

```



The API returns JSON containing its name, version, and description.



\## API Endpoint

\- \*\*URL:\*\* `http://localhost:5001/about`

\- \*\*Method:\*\* GET

\- \*\*Purpose:\*\* Returns information about the Simple REST API.



\## Screenshots

1\. `screenshots/01-network-created.png`

2\. `screenshots/02-containers-running.png`

3\. `screenshots/03-container-connectivity.png`

4\. `screenshots/04-flask-api-response.png`



\## Result

Successfully created a user-defined bridge network and ran the Flask, MySQL, and Redis containers on it. Verified container name resolution and tested the Flask API endpoint.



