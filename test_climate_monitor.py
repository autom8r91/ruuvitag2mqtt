import pytest
import yaml

from climate_monitor import ClimateMonitor
from data_formatter import DataFormatter


@pytest.fixture
def config():
    with open('/etc/climate-monitor/config.yaml') as f:
        return yaml.safe_load(f)


def test_climate_monitor(config, mocker):
    mqtt_client = mocker.Mock()
    data_formatter = mocker.Mock()
    monitor = ClimateMonitor(config)
    monitor.mqtt_client = mqtt_client
    monitor.data_formatter = data_formatter
    monitor.run()

    mqtt_client.connect.assert_called_once_with(config['mqtt']['host'], config['mqtt']['port'])
    mqtt_client.username_pw_set.assert_called_once_with(config['mqtt']['username'], config['mqtt']['password'])
    mqtt_client.publish.assert_called_once_with(config['mqtt']['topic'], 'formatted_data')


def test_data_formatter_create(config):
    formatter = DataFormatter.create(config['data_format'])
    assert isinstance(formatter, DataFormatter)
