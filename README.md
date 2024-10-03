# BragApp

This repository contains frontend and backend for **BragApp**, a showcase solution that use [immuDB Vault API](https://vault.immudb.io/). The frontend is built using **Vue.js**, while the backend is powered by **FastAPI**. This application is containerized using Docker to facilitate easy setup and development.

## Key Features:
- API Documentation: All APIs come with their instruction manual, written better than IKEA intructions.
- Docstring Documentation: PEP 257 compliant.
- Design Patterns Applied: The code not only works but does it in style. 
- Sandbox enviroment
- Backend Testing: Pytest has given its seal of approval.
- Frontend Testing with Vitest: there's not much to test, but I had to do something!
- Python Module for Consuming immuDB Vault APIs.
- Everything Executable with Dockers, orchestrated with Docker Compose. 
- A Decent GUI: It's not fancy,  but hey, it works!
- Exception Handling: You can’t ask for more in a showcase, right?
- Easy peasy Solution to Initialize a Collection in the Vault. You can’t ask for more in a showcase, right?

## QuickStart

To get started quickly, you can use **Docker Compose** to build and run the entire application with a single command.

Make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)



### STEP 1. **Clone the repository**:
```bash
docker-compose up --build
```

### STEP 2. **Setup enviroment variables**:

Create a new *".env"* file inside the backend folder. Insert you immuDB Vault API key, or set the IMMUDB_VAULT_SANDBOX flag to 1 if you want to test the application without using any real immudb vault.

```bash
# .env
IMMUDB_VAULT_SANDBOX=0
IMMUDB_VAULT_LEDGER_NAME=default
IMMUDB_VAULT_COLLECTION_NAME=test
IMMUD_DB_URL=https://vault.immudb.io/ics/api/v1
IMMUD_DB_API_KEY="your-api-key"
FRONTEND_URL=http://localhost:8080
EOL
```
    
    
Create a new *".env"* file inside the frontend folder. 

```bash
# .env
VITE_BRAGAPP_API_BASE_URL=http://localhost:8080/
```

### STEP 3. **Build and start**:
```bash
cd BragApp
docker-compose up --build
```

### STEP 4. **Access the application**:
- **Frontend**: http://localhost:8080
- **Backend**: http://localhost:5000
- **Backend Docs**: http://localhost:5000/docs


## Frontend
For more details on the frontend setup, development environment, and available scripts, refer to the [frontend README](.frontend/README.md).

## Backend
For more details on the backend setup, environment configuration, and available endpoints, refer to the [backend README](.backend/README.md).

## License
This project is licensed under the MIT License. See the LICENSE file for details.

