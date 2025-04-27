# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY requirements.txt .
COPY trading_pull.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Disable SSL warnings (optional: for local dev)
ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"

# Run the script
CMD ["python", "trading_pull.py"]

