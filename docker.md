---
title: Docker Cheatsheet
---

Docker Cheatsheet
-----------------

```bash
# List containers
$ docker ps
```

```bash
# List images
$ docker images
```

```bash
# Remove one or more images
$ docker rmi [IMAGE...]
```

```bash
# Build an image from a Dockerfile

# -t, --tag
# Name and optionally a tag in the 'name:tag' format

$ docker build [OPTIONS] PATH
```

```bash
# Stop one or more running containers
$ docker stop CONTAINER

# Stop all running containers
$ docker stop $(docker ps -a -q)
```
