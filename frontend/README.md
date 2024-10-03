# BragApp Frontend

## Description

This project is a **Vue.js 3** and **Vite**-powered frontend application designed a showcase. It includes Docker configuration and a testing environment using Vitest. 

In the AddAccount view, you can't find the IBAN field validation on the frontend. I’ve bent Best Practices here to let you easily explore how the system behaves when the API throws specific errors. So, feel free to enter whatever you like and watch the magic happen!

## Project Structure

```bash
frontend/
├── .env                    # Environment variable configuration
├── .gitignore               # Git file exclusion rules
├── Dockerfile               # Docker container definition
├── index.html               # Main HTML entry file
├── package.json             # Project dependencies and scripts
├── README.md                # Project documentation
├── vite.config.js           # Vite configuration
├── vitest.config.js         # Vitest testing configuration
├── public/
│   └── favicon.ico          # Website icon
└── src/
    ├── assets/              # Stylesheets and static resources
    │   ├── base.css
    │   └── main.css
    ├── components/          # Vue components
    │   ├── AccountModal.vue
    │   ├── Navbar.vue
    │   └── __tests__/       # Component unit tests
    │       └── AccountModal.test.js
    ├── router/              # Vue Router configuration
    │   └── index.js
    ├── views/               # App pages and views
    │   ├── AccountList.vue
    │   └── AddAccount.vue
    └── main.js              # Application entry point
```

## Prerequisites

Ensure you have the following tools installed before starting:

- [Node.js](https://nodejs.org/) (version 20.x or higher)
- [Docker](https://www.docker.com/) (optional, for container-based execution)
- [Git](https://git-scm.com/)

## Quick Start

1. Clone the repository:

```bash
git clone <repository-url>
cd BragApp/frontend
```

2. Install the dependencies:

```bash
npm install
```

3. Create an .env file in the root directory with this content:

```bash
# .env
VITE_BRAGAPP_API_BASE_URL=http://localhost:8080/
```

4. Start the local development server:

```bash
npm run dev
```

The application will be available at [http://localhost:8080](http://localhost:8080).



## Docker Support

To run the application inside a Docker container, use the following commands:

```bash
docker build -t <image-name> .
docker run -p 8080:8080 -d --restart unless-stopped bragapp_frontend
```

This will run the application inside a container and expose it on port 5000.

## Testing

This project uses **Vitest**. The tests are located in the `src/components/__tests__` directory.

To run the tests:

```bash
npm run test:unit
```

You can modify the test configurations inside `vitest.config.js` as needed.

## License

This project is licensed under the MIT License.
