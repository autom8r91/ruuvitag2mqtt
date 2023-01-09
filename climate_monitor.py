import logging
import yaml
from ruuvitag_sensor.ruuvi import RuuviTagSensor
from paho.mqtt.client import Client
from data_formatter import DataFormatter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ClimateMonitor:
    """Collects data from RuuviTags and forwards it via MQTT.

    Attributes:
        - config (dict): Configuration for the climate monitor.
        - mqtt_client (paho.mqtt.client.Client): MQTT client used to publish data.
        - data_formatter (DataFormatter): Formatter for the chosen data format.
    """
    def __init__(self, config_path: str):
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

        self.mqtt_client = Client()
        self.data_formatter = DataFormatter.create(self.config['data_format'])

        # Set MQTT client options
        self.mqtt_client.username_pw_set(self.config['mqtt']['username'], self.config['mqtt']['password'])
        self.mqtt_client.connect(self.config['mqtt']['host'], self.config['mqtt']['port'])

    def run(self):
        """Collects data from RuuviTags and publishes it via MQTT."""
        # Get a list of RuuviTags that are currently in range
        ruuvitags = RuuviTagSensor.get_ruuvitags()
        if not ruuvitags:
            logger.warning('No RuuviTags found')
            return

        # Collect data from each RuuviTag and publish it via MQTT
        for ruuvitag in ruuvitags:
            data = ruuvitag.update()
            if not data:
                continue
            payload = self.data_formatter.format(data)
            self.mqtt_client.publish(self.config['mqtt']['topic'], payload)
            logger.info(f'Published data from RuuviTag {data["device"]}')
