FROM mongo:6.0.3
EXPOSE 27017

ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=root