# Dockerfile Cheat Sheet

## FROM

- **Meaning:** Specifies the base image to start from.
- **Example:** `FROM python:3.9`

## RUN

- **Meaning:** Executes a command during the build process.
- **Example:** `RUN pip install -r requirements.txt`

## COPY

- **Meaning:** Copies files or directories from the host to the image.
- **Example:** `COPY . /app`

## WORKDIR

- **Meaning:** Sets the working directory for subsequent commands.
- **Example:** `WORKDIR /app`

## ENV

- **Meaning:** Sets environment variables in the image.
- **Example:** `ENV DEBUG=True`

## EXPOSE

- **Meaning:** Exposes a port when the container runs.
- **Example:** `EXPOSE 8000`

## CMD

- **Meaning:** Specifies the command to run when a container starts.
- **Example:** `CMD ["gunicorn", "myapp.wsgi:application", "-b", "0.0.0.0:8000"]`

## ENTRYPOINT

- **Meaning:** Configures a command to run as the main process.
- **Example:** `ENTRYPOINT ["python", "app.py"]`

## VOLUME

- **Meaning:** Creates a mount point for external volumes.
- **Example:** `VOLUME /data`

## Dockerfile Advanced

## ARG

- **Meaning:** Defines build-time variables.
- **Example:** `ARG ENVIRONMENT=production`

## ONBUILD

- **Meaning:** Adds a trigger instruction to be executed later.
- **Example:** `ONBUILD COPY . /app`

## HEALTHCHECK

- **Meaning:** Specifies a command to check container health.
- **Example:** `HEALTHCHECK CMD curl --fail http://localhost:8000/ || exit 1`

## USER

- **Meaning:** Sets the user for subsequent commands.
- **Example:** `USER myuser`

## LABEL

- **Meaning:** Adds metadata to an image.
- **Example:** `LABEL maintainer="john@example.com"`
