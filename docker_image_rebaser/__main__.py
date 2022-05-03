import logging
import argparse

from images import initiate_docker_client
from images import pull_image
from images import retag_image
from images import push_image

from helper import parse_image_input

logging.basicConfig(format='docker_image_rebaser | %(levelname)s | %(message)s ',
                    encoding='utf-8', level=logging.INFO)


def main():

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description="""
Docker Image Rebaser

This tool enables you to transfer images from any open registry like Docker or Quay to another registry.

If you are using Docker Desktop for Windows, make sure you enable the "Expose daemon on tcp://localhost:2375 without TLS" under the general settings tab in Docker Desktop.

Make sure you are logged in to the repository you want to push the image to. Use for example docker login for Docker hub or gcloud auth configure-docker <URL> for Google Artifact Registry.
    """)
    parser.add_argument('-s', '--socket',
                        help='specify socket to connect to', required=True)
    parser.add_argument('-i', '--image',
                        help='specify image to pull', required=True)
    parser.add_argument('-n', '--new-image',
                        help='specify new image name', required=True)
    parser.add_argument('-r', '--registry',
                        help='specify destination registry', required=True)
    parser.add_argument('-d', '--debug',
                        help='enable debugging on logger', action='store_true')

    args = parser.parse_args()

    if args.debug:

        logging.getLogger().setLevel(logging.DEBUG)
        logging.info('Log level changed to DEBUG')

    client = initiate_docker_client(args.socket)

    image = parse_image_input(args.image)

    new_image_name = parse_image_input(args.new_image)

    registry = "".join([args.registry.lower(), f"/{new_image_name[0]}"])

    if len(image) == 2:
        pull_image(client.images, image[0], tag=image[1])
        retag_image(client.images, image, registry)
        push_image(client.images, new_image_name[1], registry)
    else:
        pull_image(client.images, image[0]).tag(registry)
        retag_image(client.images, [image[0], "latest"], registry)
        push_image(client.images, "latest", registry)


if __name__ == '__main__':

    main()
