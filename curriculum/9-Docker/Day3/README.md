# Lesson: React.js + Django API + PostgreSQL in Docker

## Introduction to Docker

When Docker is integrated with Vite + React, developers experience an unparalleled development and deployment workflow. Docker provides a unified environment, ensuring that the Vite + React application performs consistently, whether in development, testing, or production stages. The containerized setup eliminates discrepancies between development and production environments, addressing the infamous "it works on my machine" dilemma and fostering seamless collaboration among team members.

Moreover, Docker's containerization allows for efficient resource utilization and effortless scaling of Vite + React applications. Developers can confidently deploy their web applications, knowing they will operate consistently across various platforms, from local development machines to cloud-based servers.

## Learning Objectives

- Understand what Docker is and its role in application deployment.
- Create a Dockerfile to define the container's configuration.
- Build a Docker image from the Dockerfile.
- Run a Docker container to host the Vite + React.js project on port 80.
- Use basic Docker commands to manage containers effectively.
- Configure the Vite + React.js project to run in the Docker container.

## Concepts and Steps

### Step 1: Configure Vite + React.js Project

Before we build the Docker image, we need to configure the Vite + React.js project to run on a specific port. By default, Vite runs on port 5173 in development mode. To correctly expose the development port, update your Vite configuration.

Open the `vite.config.js` (or `vite.config.ts`) file in the root of your Vite + React.js project. Locate the `server` section and update the `port` setting to the desired port (e.g., 5173):

```javascript
// vite.config.js (or vite.config.ts)
export default defineConfig({
  server:{
    host:"0.0.0.0",
    port:5173,
  },
  plugins: [react()],
})
```

### Step 2: Create the Dockerfile

Now, let's create the Dockerfile to define the configuration of the Docker container.

Create a new file named `Dockerfile` in the root directory of your Vite + React.js project. Open the `Dockerfile` and add the following content:

```Dockerfile
# Use the official Node.js base image
FROM node:latest

# Set the working directory inside the container
WORKDIR /front_end

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the entire project to the container
COPY . .

# Build the production version of the Vite + React.js project
RUN npm run build

# Expose port 5173 to allow external access
EXPOSE 5173

# Start the Vite server to serve the built project
CMD ["npm", "run", "dev"]
```

#### Explanation:

- `FROM node:latest`: This line sets the base image for our Docker image. We're using the official Node.js image as our base.

- `WORKDIR /app`: Sets the working directory inside the container to `/app`.

- `COPY package*.json ./`: Copies the `package.json` and `package-lock.json` files from the host machine to the container's working directory.

- `RUN npm install`: Installs the project dependencies inside the container.

- `COPY . .`: Copies the entire project from the host machine to the container's working directory.

- `RUN npm run build`: Builds the production version of the Vite + React.js project inside the container.

- `EXPOSE 5173`: Exposes port 5173 on the container, allowing external access.

- `CMD ["npm", "run", "serve"]`: Specifies the command to run when the container starts. In this case, it starts the Vite server to serve the built project.

### Step 3: Build the Docker Image

With the Dockerfile in place, we can now build the Docker image for our Vite + React.js project.

Open the terminal and navigate to the directory containing the Dockerfile and your Vite + React.js project files. Then, run the following command:

```bash
docker build -t my-vite-react-app .
```

#### Explanation:

- `docker build`: This is the command to build a Docker image.
- `-t my-vite-react-app`: The `-t` flag is used to tag the image with a name (in this case, `my-vite-react-app`).
- `.`: The period `.` indicates that the Dockerfile is in the current directory.

This command will build the Docker image `my-vite-react-app` using the Dockerfile located in the current directory.

### Step 4: Run the Docker Container

Now that we have the Docker image built, we can create

 and run a Docker container based on that image.

Run the following command:

```bash
docker run -d -p 80:5173 my-vite-react-app
```

#### Explanation:

- `docker run`: This command creates and runs a Docker container based on the specified image.
- `-d`: The `-d` flag runs the container in detached mode, which means it runs in the background.
- `-p 80:5173`: The `-p` flag maps port 5173 from the container to port 80 on your local machine, allowing you to access the application at `http://localhost`.
- `my-vite-react-app`: The name of the Docker image to use when creating the container.

### Step 5: Access Your Vite + React.js Application

Congratulations! Your Vite + React.js application is now running in a Docker container and is accessible at `http://localhost` on port 80 of your local machine. You should see your application running successfully in the web browser.

### Step 6: Exiting the Docker Container

If you want to stop the Docker container, you can use the `docker stop` command. First, find the container ID or name:

```bash
docker ps
```

Locate the container ID or name in the output. Then, stop the container:

```bash
docker stop <container_id_or_name>
```

### Step 7: Starting a Container with --rm

By default, Docker retains stopped containers. If you want to automatically remove the container when it stops, you can use the `--rm` flag when running the container:

```bash
docker run -d -p 80:5173 --rm my-vite-react-app
```

#### Explanation:

- `--rm`: The `--rm` flag automatically removes the container when it stops running. This can help keep your system clean and organized.

## Conclusion

In this lesson, you've learned how to deploy a simple Vite + React.js project in a Docker container and bind it to port 80 on your local machine. You've seen the essential Docker commands and what each command does. Additionally, you've configured the Vite + React.js project to run inside the Docker container.

Docker provides a convenient way to package and deploy applications, ensuring consistency and portability across different environments. Now you can use Docker to deploy and manage more complex applications with ease. Happy coding!
