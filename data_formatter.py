import json
from typing import Dict


class DataFormatter:
    """Base class for data formatters.

    Data formatters are responsible for converting the data collected from RuuviTags
    into a specific format before it is published via MQTT.
    """

    @staticmethod
    def create(data_format: str):
        """Factory method for creating a data formatter for the specified format.

        Args:
            - data_format (str): Data format to use. Options are 'xml', 'json', and 'influxdb'.

        Returns:
            - DataFormatter: Data formatter for the specified format.
        """
        if data_format == 'xml':
            return XmlDataFormatter()
        elif data_format == 'json':
            return JsonDataFormatter()
        elif data_format == 'influxdb':
            return InfluxdbDataFormatter()
        else:
            raise ValueError(f'Invalid data format: {data_format}')

    def format(self, data: Dict):
        """Converts the collected data into the specified format.

        Args:
            - data (dict): Data collected from a RuuviTag.

        Returns:
            - str: Formatted data.
        """
        raise NotImplementedError()


class XmlDataFormatter(DataFormatter):
    def format(self, data: Dict):
        xml = ['<?xml version="1.0" encoding="UTF-8"?>']
        xml.append('<ruuvitag>')
        for key, value in data.items():
            xml.append(f'  <{key}>{value}</{key}>')
        xml.append('</ruuvitag>')
        return '\n'.join(xml)


class JsonDataFormatter(DataFormatter):
    def format(self, data: Dict):
        return json.dumps(data)


class InfluxdbDataFormatter(DataFormatter):
    def format(self, data: Dict):
        fields = ','.join([f'{key}={value}' for key, value in data.items()])
        return f'measurement,device={data["device"]} {fields}'
