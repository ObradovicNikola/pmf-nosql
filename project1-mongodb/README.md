# MongoDB project

## MongoDB setup

1. build the docker image
   - `docker build --pull --rm -f "docker/mongo.dockerfile" -t pmfnosql:latest "docker"`
2. run the image
   - `docker run -p 27017:27017 --name pmf-mongo pmfnosql:latest`

alt:

- `docker run -d -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root -p 27017:27017 --name pmf-mongo mongo:4.4.18`


<!-- mongo:5.0.14 -->
<!-- mongo:4.4.18 -->
## Data

Data is downloaded from https://www.kaggle.com/datasets/thedevastator/most-kickstarter-campaigns-fail-here-s-why
as a single csv file.
