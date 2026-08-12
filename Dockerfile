FROM python:3.12-slim

WORKDIR /app

# System dependencies required by WeasyPrint
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libcairo2 \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
        libgdk-pixbuf-2.0-0 \
        libffi-dev \
        shared-mime-info \
        fonts-dejavu \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend application
COPY . .

# Render uses the PORT environment variable.
EXPOSE 10000

# Start FastAPI
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}"]