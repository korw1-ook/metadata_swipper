FROM python:3.11-slim

# Install system dependency
RUN apt-get update && apt-get install -y exiftool

# Create app directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run server
CMD ["python", "server.py"]
