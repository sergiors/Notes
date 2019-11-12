---
title: Docker
---

```bash
# list containers
$ docker ps
```

```bash
# list images
$ docker images
```

```bash
# remove one or more images
$ docker rmi [IMAGE...]
```

```bash
# build an image from a Dockerfile

# -t, --tag
# name and optionally a tag in the 'name:tag' format

$ docker build [OPTIONS] PATH
```

```bash
# stop one or more running containers
$ docker stop CONTAINER

# stop all running containers
$ docker stop $(docker ps -a -q)
```
