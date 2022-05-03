
import docker
import time
import sys
import logging

logger = logging.getLogger(__name__)


def initiate_docker_client(base_url):
    """
    It creates a docker client object that can be used to interact with the docker daemon

    :param base_url: The URL of the Docker daemon
    :return: A docker client object.
    """

    logger.info("Connecting to the Docker client.")
    try:

        client = docker.DockerClient(base_url=base_url)
        logger.info('Client connection succesful!')
        return client

    except Exception as ex:

        logger.error(f'Unable to connect with Docker client: {ex}')
        sys.exit(1)


def pull_image(docker, name, tag="latest"):
    """
    > Pulls a docker image from the docker hub

    :param docker: The docker client object
    :param name: The name of the image to pull
    :param tag: The tag of the image to pull, defaults to latest (optional)
    :return: The image ID of the pulled image.
    """

    logger.info("Pulling image, this may take a few minutes...")
    try:
        image = docker.pull(name, tag=tag)
        logger.info('Image pull succesful!')
        return image
    except Exception as ex:

        logger.error(f'Unable to pull image: {ex}')
        sys.exit(1)


def retag_image(docker, image, repo):
    """
    It takes a docker image, and retags it with a new repository name

    :param docker: docker client
    :param image: This is the image that you want to retag. It's a tuple of the image name and the tag
    :param repo: The repository to push the image to
    """

    logger.info("Retagging image...")
    time.sleep(5)
    try:
        local_image = docker.get(f"{image[0]}:{image[1]}")
        local_image.tag(repo, tag=image[1])
        logger.info(f"New name: {''.join([repo,':', image[1]])}")
        docker.remove(f"{image[0]}:{image[1]}")
        logger.info('Image retag succesful!')
    except Exception as ex:

        logger.error(f'Unable to retag image: {ex}')
        sys.exit(1)

def push_image(docker, image, repo):
    """
    This function takes a docker image and a repository as input, and pushes the image to the repository

    :param docker: The docker client object
    :param image: The name of the image you want to push
    :param repo: The name of the repository you want to push to
    """

    logger.info("Pushing image, this may take a few minutes...")
    try:
        docker.push(repo, tag=image)
        logger.info('Image push succesful!')
    except Exception as ex:

        logger.error(f'Unable to push image: {ex}')
        sys.exit(1)
