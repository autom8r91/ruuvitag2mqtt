FROM python:3.7

WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY climate_monitor/ ./climate_monitor/

# Set environment variables
ENV PYTHONPATH="/app:${PYTHONPATH}"

# Run the climate monitor
CMD ["python", "-m", "climate_monitor"]
