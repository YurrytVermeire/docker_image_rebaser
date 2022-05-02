import docker
import getpass
import google.auth
import time

credentials, project_id = google.auth.default()

def initiate_docker_client(base_url):
    print(42*"-")
    print("Connecting to the docker client.")
    try:
        return docker.DockerClient(base_url=base_url)
    finally:
        print("Connected!")

def pull_image(local_images, name, tag="latest"):
    print(42*"-")
    print("Pulling image, this may take a few minutes.")
    try:
        return local_images.pull(name, tag=tag)
    finally:
        print("Done pulling image!")

def parse_image_input(image_string):
    parsed_string = list()
    if ":" in image_string:
        parsed_string = image_string.split(":")
    else:
        parsed_string.append(image_string)
    return parsed_string

def retag_image(docker, image, repo):
    print(42*"-")
    print("Retagging image...")
    time.sleep(5)
    local_image = docker.get(f"{image[0]}:{image[1]}")
    local_image.tag(repo, tag=image[1])
    docker.remove(f"{image[0]}:{image[1]}")
    print("Done retagging image!")
    
def push_image(docker, image, repo):
    print(42*"-")
    print("Pushing image, this may take a few minutes.")
    docker.push(repo, tag=image)
    print("Done pushing image!")

version = input("Enter your docker socket: ")
client = initiate_docker_client(version)
print(42*"-")
image = parse_image_input(input("Image: "))
repo = "".join([input("Give the new repository: ").lower(), f"/{image[0]}"])
if len(image) == 2:
    pull_image(client.images, image[0], tag=image[1])
    retag_image(client.images, image, repo)
    push_image(client.images, image[1], repo)
else:
    pull_image(client.images, image[0]).tag(repo)
    retag_image(client.images, [image[0], "latest"], repo)
    push_image(client.images, "latest", repo)