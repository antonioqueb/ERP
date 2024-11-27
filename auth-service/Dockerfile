# Use an appropriate base image
FROM python:3.10-slim

# Install curl
RUN apt-get update && apt-get install -y curl

# Install any other dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your application code
COPY . /app
WORKDIR /app

# Expose the port
EXPOSE 8002

# Set the entrypoint or command
CMD ["python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]