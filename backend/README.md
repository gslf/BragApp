# BragApp Frontend

## Description

This project is a **FastAPI** powered backend application designed a showcase. It includes Docker configuration and a testing environment. 

## Project Structure

```bash
root/
├── app/
│   ├── main.py                  # Main application file
│   ├── settings.py              # Configuration settings for the app
│   ├── utils.py                 # Utility functions
│   ├── __init__.py              # App initialization
│   ├── adapters/
│   │   ├── immudb_adapter.py          # Adapter for immudb database interactions
│   │   ├── immudb_adapter_response.py # Adapter response handling
│   │   └── __init__.py                # Adapters initialization
│   ├── immudb/
│   │   ├── client.py             # Client for immudb operations
│   │   ├── _api_client.py        # API client for immudb
│   │   ├── _production_client.py # Client for production environment
│   │   ├── _sandbox_client.py    # Client for sandbox environment
│   │   └── tests/
│   │       ├── test_production_client.py # Tests for production client
│   │       └── test_sandbox_client.py    # Tests for sandbox client
│   ├── routers/
│   │   ├── operations.py        # API routes related to operations
│   │   └── __init__.py          # Router initialization
│   └── schemas/
│       ├── account.py           # Schema for accounts
│       ├── operation_type.py    # Schema for operation types
│       └── __init__.py          # Schema initialization
│
├── tests/
│   ├── test_api.py              # API tests
│   ├── test_models.py           # Tests for models
│   └── __init__.py              # Tests initialization
│
├── requirements.txt     # Python dependencies
├── Dockerfile           # Dockerfile for building the project
├── README.md            # Project documentation
```

## Prerequisites
Before setting up the project, ensure you have the following installed:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/) (optional, for container-based execution)
- [Python](https://www.python.org/) (version 12.x or higher)
- Dependencies listed in `requirements.txt`


## Quick Start
Follow these steps to get the project up and running:

1. Clone the repository:
```bash
git clone <repository-url>
cd BragApp/backend
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Create an .env file in the root directory with this content:

```bash
cat <<EOL > .env
# .env
IMMUDB_VAULT_SANDBOX=0
IMMUDB_VAULT_LEDGER_NAME=default
IMMUDB_VAULT_COLLECTION_NAME=test
IMMUD_DB_URL=https://vault.immudb.io/ics/api/v1
IMMUD_DB_API_KEY="your-api-key"
FRONTEND_URL=http://localhost:8080
EOL
```

Set the IMMUDB_VAULT_SANDBOX flag to 1 if you want to test the application without using any real immudb vault.


4. Start the application:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## Docker Support

To run the application inside a Docker container, use the following commands:

```bash
docker build -t <image-name> .
docker run -p 5000:5000 -d --restart unless-stopped --env-file .env <image-name>
```

This will run the application inside a container and expose it on port 5000.

## Testing

```bash
pip3 install -r requirements.txt
pytest
```
