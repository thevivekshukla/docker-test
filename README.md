### Build

```shell
docker build -t docker-test --platform linux/amd64 .
```

Platform options are: `linux/amd64`, `linux/arm64`, `windows/amd64`

### Run

```shell
docker run -it docker-test python main.py
```

### Tag

```shell
docker tag docker-test username/docker-test
```

### Push

```shell
docker push username/docker-test
```
