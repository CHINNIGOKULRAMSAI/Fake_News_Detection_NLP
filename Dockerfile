# Use official Python image
FROM python:3.10-slim

# Environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Install system dependencies (needed for some Python packages)
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies first (for better layer caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data used by your app
RUN python -m nltk.downloader stopwords wordnet

# Copy the rest of the project
COPY . .

# Expose the port Uvicorn will listen on
EXPOSE 8000

# Start FastAPI app with Uvicorn
# main:app  ->  main.py file, "app" variable inside it
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
