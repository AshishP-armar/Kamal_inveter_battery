# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local code into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the app port
EXPOSE $PORT

# Run the Flask app with Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:$PORT", "--timeout", "120", "--workers", "1"]
