docker build . -t docker-test --platform linux/amd64

docker tag docker-test username/docker-test

docker push username/docker-test
