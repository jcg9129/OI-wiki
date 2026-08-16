This page describes how to deploy the **OI Wiki** environment using Docker.

???+ warning "Warning"
    The steps below must be run as the root user or as a user in the docker group.

## Pull the **OI Wiki** image

```bash
# Run one of the following commands on the host
# Docker Hub image (official registry)
docker pull 24oi/oi-wiki
# DaoCloud Hub image (China mirror registry)
docker pull daocloud.io/sirius/oi-wiki
# Tencent Hub image (China mirror registry)
docker pull ccr.ccs.tencentyun.com/oi-wiki/oi-wiki
```

## Build the image yourself

```bash
# Run the following commands on the host
# Clone the Git repository
git clone https://github.com/OI-wiki/OI-wiki.git
cd OI-wiki/
# Build the image
docker build -t [name][:tag] . --build-arg [variable1]=[value1] [variable2]=[value2]...
```

-   (Required) Set `[name]` to set the image name; (optional) set `[tag]` to set the image tag (if set, the image name at run time consists of both parts).
-   You can set environment variables via the `--build-arg` parameter.

Available environment variables:

-   Set `WIKI_REPO` to use a mirror site of the wiki repository (GitHub is used automatically when unset).
-   Set `PYPI_MIRROR` to use a mirror site of the PyPI repository (the official PyPI is used automatically when unset).
    -   Within China, we recommend the TUNA mirror `https://pypi.tuna.tsinghua.edu.cn/simple/`.
-   Set `LISTEN_IP` to change the listening IP (`0.0.0.0` when unset, i.e. listening on all IPs).
-   Set `LISTEN_PORT` to change the listening port (`8000` when unset).

Example:

```bash
docker build -t OI_Wiki . --build-arg WIKI_REPO=https://hub.fastgit.xyz/OI-wiki/OI-wiki.git PYPI_MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple/
# Build an image named OI_Wiki (default tag), using the FastGit service to speed up cloning and the TUNA mirror.
```

## Run the container

```bash
# Run the following command on the host
docker run -d -it [image]
```

-   (Required) Set `[image]` to set the image. For example, an image pulled from Docker Hub is `24oi/oi-wiki`, and one pulled from DaoCloud Hub is `daocloud.io/sirius/oi-wiki`.
-   (Required) Set `-p [port]:8000` to map the container port to a host port (without this statement, no port is exposed by default; when setting it, replace `[port]` with the host port). Once set, you can access **OI Wiki** on the host at `http://127.0.0.1:[port]`.
-   Set `--name [name]` to set the container name. (Empty by default. When setting it, replace `[name]` with a custom container name. To view the container id, run `docker ps`.)

## Use the container

???+ note "Note"
    The example is deployed based on Ubuntu latest.

Enter the container:

```bash
# Run the following command on the host
docker exec -it [name] /bin/bash
```

If you remove `-d` from the run command above, you enter the container's bash directly, and the container stops after you exit; with `-d` it runs in the background and you must stop it manually. The command above for entering the container is for the case where `-d` was added.

Special usage:

```bash
# Run the following commands inside the container
# Update the git repository
wiki-upd

# Use our custom theme
wiki-theme

# Build mkdocs; the static pages are produced in the site folder
wiki-bld

# Build mkdocs and render MathJax; the static pages are produced in the site folder
wiki-bld-math

# Run a server; visit http://127.0.0.1:8000 in the container or http://127.0.0.1:[port] on the host to see the result
wiki-svr

# Format Markdown
wiki-o
```

Exit the container:

```bash
# Run the following command inside the container
# Exit
exit
```

## Stop the container

```bash
# Run the following command on the host
docker stop [name]
```

## Start the container

```bash
# Run the following command on the host
docker start [name]
```

## Restart the container

```bash
# Run the following command on the host
docker restart [name]
```

## Remove the container

```bash
# Run the following command on the host
# Stop the container before removing it
docker rm [name]
```

## Update the image

Just `pull` again; usually there are no updates.

## Remove the image

```bash
# Run the following command on the host
# Remove any containers built from the oi-wiki image before removing it
docker rmi [image]
```

## Questions

If you have questions, feel free to open an [issue](https://github.com/OI-wiki/OI-wiki/issues/new/choose)!
