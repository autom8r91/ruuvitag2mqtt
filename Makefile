# Set up the development environment
setup:
	pip install -r requirements.txt

# Run the unit tests
test:
	pytest

# Run the climate monitor script
run:
	python -m climate_monitor

# Build the Docker image
build:
	docker build -t climate-monitor .

# Start the Docker container
start:
	docker run -d --name climate-monitor climate-monitor

# Stop the Docker container
stop:
	docker stop climate-monitor

# Restart the Docker container
restart: stop start

# View the logs of the Docker container
logs:
	docker logs climate-monitor

