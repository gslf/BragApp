# Use a Node base image
FROM node:20

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY . .

# Build the app for production
RUN npm run build

# Install a static server to serve the built files
RUN npm install -g serve

# Run the application on port 5000
CMD ["serve", "-s", "dist", "-l", "8080"]
