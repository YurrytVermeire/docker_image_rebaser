
import docker
import time


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
