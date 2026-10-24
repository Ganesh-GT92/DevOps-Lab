import docker

client = docker.from_env()

print("Building Docker image...")
client.images.build(path=".", tag="flask-apparmor")
print("Image built successfully.")

container = None

try:
    print("\nStarting container with AppArmor profile...")
    container = client.containers.run(
        "flask-apparmor",
        name="flask-apparmor-sdk-test",
        ports={"5000/tcp": 5000},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    print(f"Container started: {container.short_id}")

    container_info = client.api.inspect_container(container.id)
    security_options = container_info["HostConfig"].get("SecurityOpt")

    print("Requested security options:", security_options)
    print("Note: requested options do not alone prove kernel enforcement.")

except docker.errors.DockerException as error:
    print("Container could not start with the requested profile.")
    print("Docker reported:", error)

finally:
    if container is not None:
        try:
            container.stop()
            container.remove()
            print("Test container stopped and removed.")
        except docker.errors.DockerException as error:
            print("Container cleanup issue:", error)
