# Climate Monitor

A tool to deploy an indoor climate monitoring station using a RaspberryPi with Raspbian OS and RuuviTags. The RaspberryPi runs a dockered microservice that collects data via Bluetooth 4.0 and forwards it via MQTT over SSL with a choice of XML, JSON, or influxdb-lineprotocol (configurable in a `config.yaml` file).

## Installation

1. Install Docker on your RaspberryPi by following the instructions [here](https://docs.docker.com/engine/install/debian/).
2. Install Git on your RaspberryPi by running `sudo apt-get install git`.
3. Clone this repository onto your RaspberryPi by running `git clone https://github.com/<your-username>/climate-monitor.git`.
4. Navigate to the root directory of the repository and build the Docker image by running `docker build -t climate-monitor .`.
5. Run the Docker image in a container by running `docker run -d --name climate-monitor climate-monitor`.

## Usage

1. Make sure your RuuviTags are in range of your RaspberryPi and are broadcasting data.
2. Configure the MQTT settings and data format in the `config.yaml` file located in the `/etc/climate-monitor` directory.
3. Check the logs of the Docker container to ensure that the data is being collected and forwarded correctly. You can view the logs by running `docker logs climate-monitor`.

## Troubleshooting

If the data is not being collected or forwarded correctly, try the following:

- Make sure that the RuuviTags are within range of the RaspberryPi and are broadcasting data.
- Check the MQTT settings in the `config.yaml` file to make sure they are correct.
- Check the logs of the Docker container for any error messages or other information that might be helpful in debugging the issue.

If you are still experiencing issues, please open an issue on the GitHub repository or contact the maintainer for further assistance.