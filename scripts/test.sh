#! /bin/bash

docker build -t testing-image -f testing/Dockerfile .
docker run -it -d --name testing-container testing-image

docker exec testing-container pytest ./service1 --cov ./service1
docker exec testing-container pytest ./service2 --cov ./service2

docker stop testing-container
docker rm testing-container
