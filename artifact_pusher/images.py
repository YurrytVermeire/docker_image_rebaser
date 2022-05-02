
import docker
import time


def initiate_docker_client(base_url):
    """
    It creates a docker client object that can be used to interact with the docker daemon
    
    :param base_url: The URL of the Docker daemon
    :return: A docker client object.
    """
    print(42*"-")
    print("Connecting to the docker client.")
    try:
        return docker.DockerClient(base_url=base_url)
    finally:
        print("Connected!")


def pull_image(docker, name, tag="latest"):
    """
    > Pulls a docker image from the docker hub
    
    :param docker: The docker client object
    :param name: The name of the image to pull
    :param tag: The tag of the image to pull, defaults to latest (optional)
    :return: The image ID of the pulled image.
    """
    print(42*"-")
    print("Pulling image, this may take a few minutes.")
    try:
        return docker.pull(name, tag=tag)
    finally:
        print("Done pulling image!")


def retag_image(docker, image, repo):
    """
    It takes a docker image, and retags it with a new repository name
    
    :param docker: docker client
    :param image: This is the image that you want to retag. It's a tuple of the image name and the tag
    :param repo: The repository to push the image to
    """
    print(42*"-")
    print("Retagging image...")
    time.sleep(5)
    local_image = docker.get(f"{image[0]}:{image[1]}")
    local_image.tag(repo, tag=image[1])
    docker.remove(f"{image[0]}:{image[1]}")
    print("Done retagging image!")


def push_image(docker, image, repo):
    """
    This function takes a docker image and a repository as input, and pushes the image to the repository
    
    :param docker: The docker client object
    :param image: The name of the image you want to push
    :param repo: The name of the repository you want to push to
    """
    print(42*"-")
    print("Pushing image, this may take a few minutes.")
    docker.push(repo, tag=image)
    print("Done pushing image!")
