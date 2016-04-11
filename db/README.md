# Openroads db
This is a dockerfile to create the openroads db, as well as test db data.

## Running the base image
The base image has no data, only the openroads schema
```
make db
docker run -p 5432:5432 openroads-db:base
```

## Running the test image
The base image has a few boundaries and some sample data
```
make test-db
docker run -p 5432:5432 openroads-db:test
```