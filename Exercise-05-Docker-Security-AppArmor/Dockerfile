# Use the official Python runtime
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application into the container
COPY . /app

# Install Flask
RUN pip install --no-cache-dir flask

# Expose port 5000
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
