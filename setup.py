from setuptools import setup

setup(
    name='climate-monitor',
    version='0.1.0',
    packages=['climate_monitor'],
    include_package_data=True,
    install_requires=[
        'paho-mqtt==1.5.0',
        'ruuvitag-sensor==0.3.3',
        'pyyaml==5.4.1',
        'influxdb==5.3.0'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov'],
    extras_require={
        'dev': ['mypy', 'flake8']
    }
)
