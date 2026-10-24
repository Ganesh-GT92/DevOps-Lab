import docker

client = docker.from_env()

commands = [
    ["cat", "/etc/passwd"],
    ["/bin/bash", "-c", "echo Bash executed"]
]

for command in commands:
    print(f"\nTesting command: {' '.join(command)}")

    try:
        result = client.containers.run(
            "flask-apparmor",
            command=command,
            remove=True,
            security_opt=["apparmor=my-apparmor-profile"],
            stdout=True,
            stderr=True
        )

        print("Command output:")
        print(result.decode("utf-8", errors="replace"))

        print("The command completed. This does not prove AppArmor enforcement.")

    except docker.errors.DockerException as error:
        print("Container execution failed:")
        print(error)
