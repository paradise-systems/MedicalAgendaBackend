FROM python:3.12

# Set environment variables to avoid installing __pycache__ and other files

ARG SECRET_KEY
ARG PRODUCTION
ARG DATABASE_URL
ARG MINIO_URL
ARG MINIO_ACCESS_KEY
ARG MINIO_SECRET_KEY
ARG MINIO_ENDPOINT

# Set the working directory in the container to /app
WORKDIR /app
COPY pyproject.toml .

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc
RUN python -m pip install .

COPY . .

# Comando para ejecutar la aplicación
CMD ["sh", "-c", "python -m gunicorn core.wsgi"]