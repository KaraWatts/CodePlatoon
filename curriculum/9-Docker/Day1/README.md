# Lesson: PostgreSQL and Docker

## Introduction to Docker

Docker is a game-changing technology that simplifies and streamlines the deployment of various applications, including databases like PostgreSQL. When used to deploy a PostgreSQL container, Docker provides a lightweight, portable, and isolated environment, ensuring seamless database management and easy scalability. By encapsulating PostgreSQL and its dependencies within a single container, developers can eliminate compatibility issues, ensuring consistent performance across different environments. This approach also simplifies versioning, making it easier to manage updates and rollbacks of the database. Moreover, Docker's containerization enables efficient resource utilization and rapid deployment, allowing teams to focus on developing and maintaining PostgreSQL without worrying about intricate infrastructure configurations. Whether for development, testing, or production environments, Docker's versatility in deploying PostgreSQL containers makes it an invaluable tool for modern data-driven applications.

## Learning Objectives

- Create a Dockerfile to define the configuration of the PostgreSQL database container.
- Build a Docker image from the Dockerfile.
- Run a Docker container with the PostgreSQL database and bind it to port 5433.
- Use basic Docker commands to manage containers effectively.
- Connect to the PostgreSQL database and perform administrative tasks with SUPERUSER rights.

### Docker Basics

#### 1. Dockerfile

A Dockerfile is a text file that contains a set of instructions to build a Docker image. The image serves as a blueprint for creating containers. Each instruction in the Dockerfile defines a layer in the image, and Docker uses caching to optimize the build process.

#### 2. Docker Image

A Docker image is a read-only template that includes the application code and all its dependencies. It is created from the Dockerfile and serves as the foundation for running containers.

#### 3. Docker Container

A Docker container is an instance of a Docker image that runs as a separate, isolated process. Containers provide an environment where the application can run consistently, regardless of the host system.

## Concepts and Steps

### Step 1: Create the Dockerfile

To deploy a PostgreSQL database in a Docker container, we need to create a Dockerfile to define the container's configuration.

Create a new file named `Dockerfile` in a new directory (e.g., `postgres-container`) on your local machine. Open the `Dockerfile` and add the following content:

```Dockerfile
# Use the official PostgreSQL base image
FROM postgres:latest

# Set environment variables for the PostgreSQL database
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

# Expose port 5432 for PostgreSQL
EXPOSE 5432

# Enable SUPERUSER rights for the database
ENV POSTGRES_DB=mydb
ENV POSTGRES_INITDB_ARGS="--encoding=UTF-8 --lc-collate=C --lc-ctype=C --data-checksums"

# Start the PostgreSQL server
CMD ["postgres"]
```

#### Explanation:

- `FROM postgres:latest`: This line sets the base image for our Docker image, using the official PostgreSQL image.

- `ENV POSTGRES_USER=<your user>`: Sets the environment variable `POSTGRES_USER` to define the PostgreSQL superuser's username.

- `ENV POSTGRES_PASSWORD=<password>`: Sets the environment variable `POSTGRES_PASSWORD` to define the password for the PostgreSQL superuser.

- `EXPOSE 5432`: Exposes port 5432 on the container to allow access to the PostgreSQL database.

- `ENV POSTGRES_DB=container_todo_db`: Sets the environment variable `POSTGRES_DB` to define the name of the initial database.

- `ENV POSTGRES_INITDB_ARGS="--encoding=UTF-8 --lc-collate=C --lc-ctype=C --data-checksums"`: Configures the PostgreSQL server with additional arguments during the initialization process to enable SUPERUSER rights.

  - --encoding=UTF-8: Specifies the character encoding used for the database. In this case, it is set to UTF-8, which is a widely used character encoding for multilingual support.

  - --lc-collate=C: Sets the collation order for the database. By using C, the default collation is set to the C locale, which is a simple byte-for-byte comparison and is generally faster than more complex collations.

  - --lc-ctype=C: Sets the character classification for the database. Similar to the collation, using C sets the default character classification to the C locale.

  - --data-checksums: Enables data checksums for the database. This feature ensures data integrity by calculating checksums for data pages and validating them during read operations.

- `CMD ["postgres"]`: Specifies the command to run when the container starts, which starts the PostgreSQL server.

### Step 2: Build the Docker Image

With the Dockerfile in place, we can now build the Docker image for our PostgreSQL database.

Open the terminal and navigate to the directory containing the `Dockerfile`. Then, run the following command:

```bash
docker build -t my-postgres-container .
```

#### Explanation:

- `docker build`: This is the command to build a Docker image.
- `-t my-postgres-container`: The `-t` flag is used to tag the image with a name (in this case, `my-postgres-container`).
- `.`: The period `.` indicates that the Dockerfile is in the current directory.

This command will build the Docker image `my-postgres-container` using the Dockerfile located in the current directory.

### Step 3: Run the Docker Container

Now that we have the Docker image built, we can create and run a Docker container based on that image.

Run the following command:

```bash
docker run -d -p 5433:5432 --rm --name my-postgres-db my-postgres-container
```

#### Explanation:

- `docker run`: This command creates and runs a Docker container based on the specified image.
- `-d`: The `-d` flag runs the container in detached mode, which means it runs in the background.
- `-p 5433:5432`: The `-p` flag maps port 5432 from the container to port 5433 on your local machine, allowing you to access the PostgreSQL database at `localhost:5433`.
- `--name my-postgres-db`: The `--name` flag assigns a name (`my-postgres-db`) to the container for easier identification.
- `--rm`: The `--rm` flag automatically removes the container when it stops running. This can help keep your system clean and organized.

### Step 4: Access the PostgreSQL Database

Congratulations! Your PostgreSQL database is now running in a Docker container with full SUPERUSER rights and is accessible at `localhost:5433` on your local machine.

You can use your favorite PostgreSQL client (e.g., `psql`, `pgAdmin`, or `DBeaver`) to connect to the database. Use the following connection details:

- Host: `localhost`
- Port: `5433`
- Username: `myuser` (as defined in the Dockerfile)
- Password: `mypassword` (as defined in the Dockerfile)

```bash
psql -h localhost -p 5433 container_todo_db #this command will only work if the username matches the username in your shell
```

### Step 5: Exiting the Docker Container

If you want to stop the Docker container, you can use the `docker stop` command. First, find the container ID or name:

```bash
docker ps
```

Locate the container ID or name in the output. Then, stop the container:

```bash
docker stop my-postgres-db
```

## Conclusion

In this lesson, you've learned how to deploy a PostgreSQL database in a Docker container with full SUPERUSER rights and bind it to port 5433 on your local machine. You've seen the essential Docker commands and what each command does. Additionally, you've configured the PostgreSQL database to run inside the Docker container.

Docker allows you to easily create and manage isolated environments for various applications, including databases, providing consistency and portability across different environments. Now you can use Docker to deploy and manage PostgreSQL databases with ease. Happy coding!
