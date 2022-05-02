# Docker Image Rebaser

This tool enables you to transfer images from any open registry like Docker or Quay to another repository.

## Usage

If you are using Docker Desktop for Windows, make sure you enable the "Expose daemon on tcp://localhost:2375 without TLS" under the general settings tab in Docker Desktop.

Make sure you are logged in to the repository you want to push the image to. Use for example ```docker login``` for Docker hub or ```gcloud auth configure-docker <URL>``` for Google Artifact Registry.

```bash
python(3) docker_image_rebaser
```

After executing the previous command, the package will prompt for the docker socket. This is on Windows ```tcp://localhost:2375``` and on Linux by default ```unix://var/run/docker.sock```

Next up, enter the full image name you want to rebase (enter the text after the ```docker pull``` command).
Now enter the new name you want to give the image.
And at last, enter the new repository name.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## TODO

- Error handling
- Helmcharts Yaml integration

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)