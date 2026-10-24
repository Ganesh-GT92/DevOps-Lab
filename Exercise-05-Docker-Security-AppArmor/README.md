# Exercise 05: Docker Security with AppArmor and Python

## Objective
Build and run a Flask application in Docker, request an AppArmor security profile through Docker, and test container commands using the Docker SDK for Python.

## Project Files
- `app.py` - Flask web application.
- `Dockerfile` - Instructions to build the Flask image.
- `my-apparmor-profile` - AppArmor profile source file.
- `apply_apparmor.py` - Builds the image, requests the profile when starting a container, and inspects the container configuration.
- `test_restricted_actions.py` - Tests reading `/etc/passwd` and executing Bash.
- `screenshots/` - Evidence of application and test execution.

## Implementation and Results
1. Built the Docker image named `flask-apparmor`.
2. Ran the Flask application and verified its response on port 5000.
3. Used the Docker SDK to request `apparmor=my-apparmor-profile`.
4. Inspected Docker's reported `HostConfig.SecurityOpt`.
5. Tested `cat /etc/passwd` and `/bin/bash -c "echo Bash executed"` in separate containers.

## Observed Results
Both restricted-action test commands completed successfully. Docker reported the requested AppArmor security option, but this does not establish that the profile was loaded or enforced by the kernel.

The current Windows Docker Desktop and Ubuntu WSL environment reported that AppArmor was unavailable in the WSL kernel. Therefore, kernel-level AppArmor enforcement could not be verified in this environment.

## Questions and Answers

### 1. What is the purpose of AppArmor?
AppArmor is a Linux security mechanism that applies access-control policies to restrict what programs can access or do.

### 2. How does an AppArmor profile improve security?
A correctly loaded and enforced profile can limit a program's file access, capabilities, and other permitted operations.

### 3. Which directories does this project profile attempt to restrict?
The profile denies specified access modes under `/etc/`, `/root/`, `/proc/`, and `/sys/`. The actual restrictions depend on the profile being valid, loaded, and enforced.

### 4. How can the configured security option be inspected?
The Python script inspects the container's `HostConfig.SecurityOpt` value. This verifies the requested configuration, not kernel enforcement.

### 5. Were the restricted actions blocked?
No. Both `cat /etc/passwd` and the Bash test succeeded in this environment. AppArmor enforcement was not verified.

## Conclusion
The Flask image, Docker SDK scripts, and AppArmor profile source were prepared and tested. The requested security option was accepted by Docker, but AppArmor enforcement requires verification in a compatible Linux environment where AppArmor is available and the profile is loaded.
