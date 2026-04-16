FROM python:3

WORKDIR /app

# Install system dependencies (if any)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential && \
#     rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the image
COPY . .

# Ensure the test runner script is executable
RUN chmod +x docker_test_runner.py

ENTRYPOINT ["python", "docker_test_runner.py"]