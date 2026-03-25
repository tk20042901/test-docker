This README is designed to be a "plug-and-play" guide for anyone (including future you) who needs to get this app running on a new machine.

-----

# 🚀 FastAPI Docker Application

This project is a containerized FastAPI application. It uses **Docker** to ensure the environment is consistent and **Docker Compose** to manage environment variables and local development volumes.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

  * [Docker](https://docs.docker.com/get-docker/)
  * [Docker Compose](https://docs.docker.com/compose/install/)

-----

## 🛠️ Setup & Installation

### 1\. Environment Configuration

The application requires an API key to function. Create a `.env` file in the root directory:

```bash
touch .env
```

Open the `.env` file and add your credentials:

```text
OPENAI_API_KEY=your_secret_key_here
DEBUG=True
```

### 2\. Launch the Application

To build the image and start the container, run:

```bash
docker-compose up --build
```

> **Note:** The `--build` flag ensures that any changes to your `requirements.txt` or `Dockerfile` are applied.

### 3\. Access the App

Once the logs show `Application startup complete`, you can access the app at:

  * **Main API:** [http://localhost:8080](https://www.google.com/search?q=http://localhost:8080)
  * **Interactive Docs (Swagger UI):** [http://localhost:8080/docs](https://www.google.com/search?q=http://localhost:8080/docs)

-----

## 🏗️ Development Workflow

### Hot Reloading

The `docker-compose.yml` is configured with **Volumes**. This means you can edit files in the `/app` or `/templates` folders on your local machine, and the changes will reflect inside the container **instantly** without needing a restart.

### Stopping the App

To stop the containers, press `CTRL+C` in your terminal or run:

```bash
docker-compose down
```

### Checking Environment Variables

To verify that your API key was loaded correctly inside the running container:

```bash
docker exec fastapi_app printenv OPENAI_API_KEY
```

-----

## 📂 Project Structure

```text
.
├── app/                # FastAPI Python code
├── templates/          # HTML templates
├── .env                # Secret keys (Do not commit!)
├── Dockerfile          # Image build instructions
├── docker-compose.yml  # Service orchestration
└── requirements.txt    # Python dependencies
```

-----

