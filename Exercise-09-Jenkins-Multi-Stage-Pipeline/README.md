# Exercise 09: Jenkins Multi-Stage Pipeline

## Objective
Design, configure, and execute an automated **Jenkins Multi-Stage Pipeline** that implements complete CI/CD stages (**Build**, **Test**, **Deploy**, **Run Application**, and **Test Application**) for a Python Flask microservice, demonstrating automated testing, mock staging deployment, background process management, and post-execution cleanup.

---

## Directory Structure and Files
```text
Exercise-09-Jenkins-Multi-Stage-Pipeline/
├── app.py                  # Python Flask web application
├── requirements.txt        # Python dependency manifest
├── test_app.py             # Unit test suite verifying endpoints and status codes
├── Jenkinsfile             # Declarative multi-stage Jenkins pipeline definition
├── README.md               # Documentation, pipeline stage analysis, and test results
└── screenshots/            # Verification screenshots
    ├── 01-pipeline-configuration.png
    ├── 02-pipeline-stage-view.png
    └── 03-pipeline-console-output.png
```

---

## Pipeline Architecture & Stages

1. **Stage 1 — Build**:
   - Prepares the workspace environment and validates `python3` and `flask` availability.
2. **Stage 2 — Test**:
   - Executes unit tests via `python3 test_app.py` to validate HTTP response content and status code `200 OK`.
3. **Stage 3 — Deploy**:
   - Deploys application artifacts into a dedicated release directory (`python-app-deploy/`).
4. **Stage 4 — Run Application**:
   - Launches Flask in background (`nohup`) and captures the process PID.
5. **Stage 5 — Test Application**:
   - Runs post-deployment integration validation against the active application.
6. **Post Actions (`always`, `success`, `failure`)**:
   - Safely terminates background processes via captured PID and logs execution status.

---

## Verification Evidence & Screenshots

| Evidence | Screenshot File | Description |
|---|---|---|
| **Pipeline Configuration** | `screenshots/01-pipeline-configuration.png` | Displays Pipeline job configuration in Jenkins |
| **Pipeline Stage View** | `screenshots/02-pipeline-stage-view.png` | Displays green Stage View visualization with all 5 stages passing |
| **Console Output** | `screenshots/03-pipeline-console-output.png` | Displays console log showing successful build and `Finished: SUCCESS` |

---

## Console Output Log
```text
[Pipeline] stage (Build)
Stage 1: Building and preparing application environment...
[Pipeline] stage (Test)
Stage 2: Running unit tests...
Ran 1 test in 0.003s - OK
[Pipeline] stage (Deploy)
Stage 3: Deploying application to mock environment...
[Pipeline] stage (Run Application)
Stage 4: Starting application in background...
[Pipeline] stage (Test Application)
Stage 5: Verifying deployed application...
Ran 1 test in 0.002s - OK
[Pipeline] End of Pipeline
Pipeline completed successfully!
Finished: SUCCESS
```
