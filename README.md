```shell
docker build . -t docker-test --platform linux/amd64
```

```shell
docker tag docker-test username/docker-test
```

```shell
docker push username/docker-test
```
