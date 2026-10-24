# Exercise 08: Jenkins Hello World Job

## Objective
Create, configure, and execute a Jenkins Freestyle build job that checks out a repository or executes a shell script (`hello-world.sh`), demonstrating basic automation, console log tracking, and build verification.

---

## Files in this Exercise
```text
Exercise-08-Jenkins-Hello-World/
├── hello-world.sh          # Executable shell script outputting "Hello, Jenkins!"
├── README.md               # Exercise documentation and execution logs
└── screenshots/            # Verification screenshots
    ├── 01-job-configuration.png
    └── 02-console-output.png
```

---

## Implementation & Execution Steps

### 1. The Script (`hello-world.sh`)
```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

### 2. Jenkins Freestyle Job Configuration
1. Open Jenkins at `http://localhost:8080`.
2. Click **New Item** → Name: `HelloWorld` → Select **Freestyle project** → Click **OK**.
3. Under **Description**, enter:
   ```text
   Hello World! Jenkins job.
   ```
4. Under **Build Steps**, click **Add build step** → **Execute shell**:
   ```bash
   echo "Hello, Jenkins!"
   ```
5. Click **Save**.

### 3. Build Trigger & Execution
- Click **Build Now** on the job page.
- Navigate to the build history and click **Build #1** → **Console Output**.

---

## Verification Evidence & Screenshots

| Evidence | Screenshot File | Description |
|---|---|---|
| **Job Configuration** | `screenshots/01-job-configuration.png` | Displays Freestyle job configuration and build step |
| **Console Output** | `screenshots/02-console-output.png` | Displays console log confirming `Hello, Jenkins!` and `Finished: SUCCESS` |

---

## Console Output Log
```text
Started by user Admin
Building in workspace /var/jenkins_home/workspace/HelloWorld
[HelloWorld] $ /bin/sh -xe /tmp/jenkins8472910382.sh
+ echo 'Hello, Jenkins!'
Hello, Jenkins!
Finished: SUCCESS
```
