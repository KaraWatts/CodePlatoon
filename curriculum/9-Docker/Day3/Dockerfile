# Use an official Node.js image as the base image
FROM node:latest

# Set the working directory within the container
WORKDIR /front_end

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Build the Vite React application
RUN npm run build

# Expose port 5173 for the application
EXPOSE 5173

# Environment variable to specify the Django backend URL
ENV REACT_APP_BACKEND_URL=http://api:8000

# Command to start the application
CMD ["npm", "run", "dev"]
