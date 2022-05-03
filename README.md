# Docker Image Rebaser

This tool enables you to transfer images from any open registry like Docker or Quay to another registry.

## Usage

If you are using Docker Desktop for Windows, make sure you enable the "Expose daemon on tcp://localhost:2375 without TLS" under the general settings tab in Docker Desktop.

Make sure you are logged in to the repository you want to push the image to. Use for example ```docker login``` for Docker hub or ```gcloud auth configure-docker <URL>``` for Google Artifact Registry.

```bash
python(3) docker_image_rebaser -h

options:
  -h, --help            show this help message and exit
  -s SOCKET, --socket SOCKET
                        specify socket to connect to
  -i IMAGE, --image IMAGE
                        specify image to pull
  -n NEW_IMAGE, --new-image NEW_IMAGE
                        specify new image name
  -r REGISTRY, --registry REGISTRY
                        specify destination registry
  -d, --debug           enable debugging on logger
```

## Example
```bash
python(3) docker_image_rebaser -s tcp://localhost:2375 -i ubuntu -n ubuntu2 -r europe-west1-docker.pkg.dev/blablabla/test
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## TODO

- Error handling
- Helmcharts Yaml integration

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
