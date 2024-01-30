# Docker Command Cheat Sheet

Here's a cheat sheet with common Docker commands that all developers should know:

1. **Images**

   - `docker image ls`: List all Docker images on the system.
   - `docker pull IMAGE_NAME:TAG`: Download a Docker image from a registry.
   - `docker build -t IMAGE_NAME:TAG PATH`: Build a Docker image from a Dockerfile in the specified build context.
   - `docker rmi IMAGE_ID`: Delete a Docker image by its ID.
   - `docker image prune`: Remove all dangling (unreferenced) images.
   - `docker image prune -a`: Remove all unused images.

2. **Containers**

   - `docker ps`: List all running containers.
   - `docker ps -a`: List all containers, including stopped ones.
   - `docker run IMAGE_NAME:TAG`: Create and start a new container from the specified image.
   - `docker run -p HOST_PORT:CONTAINER_PORT IMAGE_NAME:TAG`: Create and start a new container from the specified image, and map a port from the host to the container.
   - `docker run --name CONTAINER_NAME IMAGE_NAME:TAG`: Create and start a new container with the specified name.
   - `docker run --rm IMAGE_NAME:TAG`: Create and start a new container with the --rm flag, which automatically removes the container after it exits.
   - `docker run --link LINKED_CONTAINER:ALIAS IMAGE_NAME:TAG`: Create and start a new container with a link to another container, using an alias.
   - `docker start CONTAINER_ID`: Start a stopped container.
   - `docker stop CONTAINER_ID`: Stop a running container.
   - `docker rm CONTAINER_ID`: Delete a specific stopped container.
   - `docker container prune`: Remove all stopped containers.
   - `docker container prune -f`: Remove all stopped containers without confirmation.

   Explanation of added flags:

   - `-p HOST_PORT:CONTAINER_PORT`: Maps a port from the host machine to the container. For example, if you want to access a web server running inside the container on port 80, you can use -p 8080:80, where 8080 is the host port, and 80 is the container port.

   - `--name CONTAINER_NAME`: Allows you to specify a custom name for the container instead of letting Docker generate a random name. This can be useful for easy identification and management of containers.

   - `--rm`: This flag is used with the docker run command to automatically remove the container after it exits. It is useful when you have a temporary container that you don't need to persist once it has finished its task. This helps in keeping your system clean from unused containers.

   - `--link LINKED_CONTAINER:ALIAS`: This flag is used with the docker run command to establish a network link between two containers. The LINKED_CONTAINER is the name or ID of the container you want to link, and ALIAS is the alias name that you want to use to refer to the linked container inside the current container. This feature is useful when you need containers to communicate with each other over the network.

3. **Logs and Monitoring**

   - `docker logs CONTAINER_ID`: Display the logs of a container.
   - `docker stats`: Display real-time container resource usage.

4. **Network**

   - `docker network ls`: List all Docker networks.
   - `docker network create NETWORK_NAME`: Create a new Docker network.
   - `docker network connect NETWORK_NAME CONTAINER_ID`: Connect a container to a network.

5. **Volumes**

   - `docker volume ls`: List all Docker volumes.
   - `docker volume create VOLUME_NAME`: Create a new Docker volume.
   - `docker volume rm VOLUME_NAME`: Delete a specific Docker volume.

6. **Cleanup**

   - `docker system prune`: Remove all unused containers, networks, and volumes.
   - `docker system prune -a`: Remove all unused containers, networks, volumes, and images.

7. **Registry**

   - `docker login`: Log in to a Docker registry.
   - `docker push IMAGE_NAME:TAG`: Upload a Docker image to a registry.

8. **Dockerfile**

   - `FROM`: Specify the base image for building the Docker image.
   - `RUN`: Execute commands during the image build process.
   - `COPY`: Copy files and directories from the host to the image.
   - `EXPOSE`: Specify the port on which the container listens.
   - `CMD`: Define the default command when running the container.

9. **Compose Commands and Common Options**

   - `docker-compose up`: Create and start containers.
   - `docker-compose down`: Stop and remove containers, networks, and volumes.
   - `docker-compose ps`: List running services.
   - `docker-compose logs`: View container logs.
   - You can use options like `-d` to run containers in the background (detached mode) or specify a specific service to manage.

Remember to replace the placeholders (e.g., IMAGE_NAME, TAG, CONTAINER_ID) with actual values when using these commands.
