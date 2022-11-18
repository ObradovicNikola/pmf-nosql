# MongoDB project

## MongoDB setup

1. build the docker image
   - `docker build --pull --rm -f "docker/mongo.dockerfile" -t pmfnosql:latest "docker"`
2. run the image
   - `docker run -p 27017:27017 --name pmf-mongo pmfnosql:latest`
