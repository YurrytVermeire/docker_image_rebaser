from images import initiate_docker_client
from images import pull_image
from images import retag_image
from images import push_image

from helper import parse_image_input


def main():

    version = input("Enter your docker socket: ")
    client = initiate_docker_client(version)

    print(42*"-")

    image = parse_image_input(input("Image: "))

    repo = "".join(
        [input("Give the new repository: ").lower(), f"/{image[0]}"])

    if len(image) == 2:
        pull_image(client.images, image[0], tag=image[1])
        retag_image(client.images, image, repo)
        push_image(client.images, image[1], repo)
    else:
        pull_image(client.images, image[0]).tag(repo)
        retag_image(client.images, [image[0], "latest"], repo)
        push_image(client.images, "latest", repo)


if __name__ == '__main__':

    main()
