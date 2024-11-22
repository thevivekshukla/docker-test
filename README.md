```shell
docker build --tag docker-test --platform linux/amd64 .
```

Platform options are: `linux/amd64`, `linux/arm64`, `windows/amd64`

```shell
docker tag docker-test username/docker-test
```

```shell
docker push username/docker-test
```
