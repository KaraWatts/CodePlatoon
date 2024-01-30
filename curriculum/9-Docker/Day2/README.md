# Lesson: Django API + PostgreSQL + Docker

## Introduction to Docker and Django

Docker's containerization offers numerous advantages for Django API developers. It provides isolation, preventing interference between different components of the application. Developers can effortlessly reproduce the same development environment on any machine with Docker support, making collaboration more efficient. Additionally, Docker's rapid deployment capabilities enable seamless scaling, allowing the Django API to handle varying workloads with ease.

The combination of Docker and Django API empowers developers to focus on writing high-quality code and building feature-rich web applications without being constrained by complex infrastructure configurations. With its ability to manage dependencies, streamline deployment, and ensure consistency, Docker serves as a foundational pillar for unleashing the full potential of Django API and driving modern web application development forward.

## Learning Objectives

- Create a Dockerfile to define the configuration of the Django application container.
- Build a Docker image from the Dockerfile.
- Set up a PostgreSQL database container and connect it to the Django API container.
- Use basic Docker commands to manage containers effectively.
- Deploy and run the Django API project connected to the PostgreSQL database using Docker.

## Starting with Django

In a previous lesson we covered how to write a Dockerfile that would build a PostgreSQL image for us to run a container that would hold a PostgreSQL database and our designated SUPERUSER with a password. Today we are going to create Dockerfile that can build a Django image for an initialized Django project and runs a Django Container utilizing a PostgreSQL database.

### 0. Creating a Django Project

Create a django project and generate a requirements.txt within the same directory as your project and apps. These files will be copied onto our Docker image and will eventually be ran within a Docker container.

### 1. Dockerfile

#### Step 1: Create the Dockerfile

Now, let's create a Dockerfile to define the configuration of the Django API container. You'll notice we already have an existing Dockerfile that will build an image for Postgres within this directory. So we will have to give these two files separate naming conventions to ensure Docker can tell the difference between each one.

Change the Dockerfile running PostgreSQL to `Dockerfile.postgres`.

Create a new file named `Dockerfile.api` in the root directory of your Django API project. Open the `Dockerfile.api` and add the following content:

```Dockerfile
# Use the official Python base image
FROM python:latest

# Set environment variables for the Django application
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory inside the container
WORKDIR /project
# updates ubuntus installer
RUN apt-get update
# Install system dependencies to interact with postgresql
RUN apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client

# COPY requirements.txt onto the Docker container
COPY requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Install Python Projects Environment dependencies
RUN pip install -r requirements.txt

# Copy the entire Django project to the container
COPY . .

# Expose port 8000 for Django development server
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

#### Explanation:

- `FROM python:3.9`: This line sets the base image for our Docker image, using the official Python image.

- `ENV PYTHONDONTWRITEBYTECODE 1`: Prevents Python from writing `.pyc` files to improve startup time.

- `ENV PYTHONUNBUFFERED 1`: Ensures that Python output is sent straight to the terminal without being buffered.

- `WORKDIR /app`: Sets the working directory inside the container to `/app`.

- `RUN apt-get update && apt-get install -y --no-install-recommends gcc postgresql-client`:

  - `apt-get update``: This command updates the package list for the package manager (APT) to ensure it has the latest information about available packages.

  - `&&`: This is a shell operator used to chain commands. It allows you to run multiple commands sequentially, and the second command is executed only if the first command succeeds (returns an exit status of 0).

  - `apt-get install -y --no-install-recommends gcc postgresql-client`: This part of the command installs two packages: gcc and postgresql-client.

    - `-y`: Automatically answers "yes" to any prompts, allowing the installation to proceed without manual intervention.
    - `--no-install-recommends`: Tells APT not to install recommended packages, reducing the number of additional packages that might be installed.

- `COPY requirements.txt .`: Copies the `requirements.txt` file from the host machine to the container's working directory.

- `RUN pip install --upgrade pip && pip install -r requirements.txt`: Installs Python dependencies from `requirements.txt`.

- `COPY . .`: Copies the entire Django project from the host machine to the container's working directory.

- `EXPOSE 8000`: Exposes port 800

0 on the container to allow access to the Django development server.

- `CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]`: Specifies the command to run when the container starts, which starts the Django development server.

### Step 3: Build the Docker Image

With the Dockerfile in place, we can now build the Docker image for our Django API project.

Open the terminal, navigate to the root directory of your Django API project (where the `Dockerfile.api` is located), and run the following command:

```bash
docker build -t django_api -f ./Dockerfile.api .
```

#### Explanation:

- `docker build`: This is the command to build a Docker image.
- `-t django_api`: The `-t` flag is used to tag the image with a name (in this case, `django_api`). The name provided after the `-t` flag will be used to identify the image later when you want to run or manage containers based on it.
- `-f ./Dockerfile.api`: The `-f` flag is used to specify the path to the Dockerfile. In this case, `./Dockerfile.api` indicates that the Dockerfile named `Dockerfile.api` is located in the current directory (`./`).
- `.`: The period (`.`) at the end specifies the build context. The build context is the set of files and directories that are sent to the Docker daemon for building the image. In this case, it indicates that the build context is the current directory where the Docker build command is executed.

This command will build the Docker image `django-api` using the Dockerfile located in the current directory.

### Step 4: Run the Django API Container

Now that we've built our Dockerfile successfully, we can run the docker image to create a container on our local machine where our Django project will be hosted on our machines port 8000.

```bash
docker run -d -p 8000:8000 --name api django_api
```

Travel to [localhost](http://localhost:8000/) where you'll be able to see the Django Rocket running.

### Step 5: Run Django API Container with PostgreSQL

Lets change our Django API project DATABASES settings to work with PostgreSQL.

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'db',  # The hostname of the PostgreSQL container (will be explained later)
        'PORT': '5432',
    }
}
```

Now that both the Django and PostgreSQL Docker images are built and the PostgreSQL container is running (if you stopped the PostgreSQL container make sure to start/run the image again before continuing), we can run a Docker container for the Django API project that links with our PostgreSQL container.

Run the following command:

```bash
docker run -d -p 8000:8000 --name api --link <name_of_postgres_container>:db django_api
```

You'll notice this generated an error around the `makemigrations` command. Well our Docker image is being built before being linked to our PostgreSQL container so it only makes sense that Docker would raise an error. Comment/Remove the `makmigrations` and `migrate` `RUN` commands from the `Dockerfile.api` to fix this error.

#### Explanation:

- `docker run`: This command creates and runs a Docker container based on the `django_api` image.
- `-d`: The `-d` flag runs the container in detached mode, which means it runs in the background.
- `-p 8000:8000`: The `-p` flag maps port 8000 from the container to port 8000 on your local machine, allowing you to access the Django API at `localhost:8000`.
- `--name api`: The `--name` flag assigns a name (`api`) to the container for easier identification.
- `--link my-postgres-db:db`: Links the Django API container to the PostgreSQL container with the name `my-postgres-db` and an alias `db`. This allows the Django API container to access the PostgreSQL database.
- `my-django-api`: The name of the Docker image to use when creating the container.

### Step 5: Migrations & Fixtures

The PostgreSQL database and Django API containers are now linked together but our migrations are not reflected on the database. We will have to enter the Django API container and migrate our migrations from our Django project

```bash
docker exec -it api python manage.py migrate
```

Now that all of our migrations are within our database we could load any fixture data we may have to ensure our api is working properly.

```bash
docker exec -it api python manage.py loaddata list.json
docker exec -it api python manage.py loaddata task.json
docker exec -it api python manage.py loaddata subtasks.json
```

### Step 6: Access the Django API

Congratulations! Your Django API project connected to the PostgreSQL database is now running in a Docker container and is accessible at `localhost:8000` on your local machine.

You can interact with the Django API and perform API requests using tools like `curl` or Postman.

### Step 7: Exiting the Docker Container

If you want to stop the Docker container, you can use the `docker stop` command. First, find the container ID or name:

```bash
docker ps
```

Locate the container ID or name in the output. Then, stop the container:

```bash
docker stop api
```

## Conclusion

In this lesson, you've learned how to deploy a Django API project connected to a PostgreSQL database using Docker. You've seen the essential Docker commands, what each command does, and how to set up the Django project to work with Docker.

Docker simplifies the deployment process and ensures consistency and portability across various environments. Now you can use Docker to deploy and manage Django applications with ease. Happy coding!
